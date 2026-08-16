import os
import threading
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuoteRequestSerializer

from django.core.cache import cache


RATE_LIMIT_SECONDS = 15 * 60  # 15 minutes


def _get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


RESEND_API_URL = "https://api.resend.com/emails"


def _send_via_resend(*, to, subject, html, text):
    """
    Sends one email via the Resend HTTP API (over HTTPS/443), which
    avoids the outbound-SMTP blocking/timeouts some hosts (e.g. Railway)
    impose on port 587/465. Raises on failure so the caller's except
    block can log it.
    """
    resp = requests.post(
        RESEND_API_URL,
        headers={
            "Authorization": f"Bearer {settings.RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "from": settings.DEFAULT_FROM_EMAIL,
            "to": [to],
            "subject": subject,
            "html": html,
            "text": text,
        },
        timeout=15,
    )
    resp.raise_for_status()


def _send_quote_emails(quote_id):
    """
    Runs on a background thread so the HTTP request doesn't block on
    email sending. Re-fetches the quote by id since this runs outside
    the request/DB-connection context that started it.
    """
    from .models import QuoteRequest

    try:
        quote = QuoteRequest.objects.get(pk=quote_id)
    except QuoteRequest.DoesNotExist:
        return

    body = (
        f"New quote request received from the website:\n\n"
        f"Name: {quote.name}\n"
        f"Company: {quote.company or '-'}\n"
        f"Email: {quote.email}\n"
        f"Phone: {quote.phone or '-'}\n"
        f"Service: {quote.service}\n\n"
        f"Message:\n{quote.message}\n"
    )

    try:
        # ---- Email 1: Notify the business (info@lithavi.com) ----
        admin_html = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <div style="background: #0a1e3f; padding: 24px;">
                <h1 style="color: #ffffff; margin: 0; font-size: 18px;">Lithavi International</h1>
            </div>
            <div style="padding: 24px; background: #f9f9f9;">
                <h2 style="color: #0a1e3f;">New Quote Request</h2>
                <p><strong>Name:</strong> {quote.name}</p>
                <p><strong>Company:</strong> {quote.company or '-'}</p>
                <p><strong>Email:</strong> {quote.email}</p>
                <p><strong>Phone:</strong> {quote.phone or '-'}</p>
                <p><strong>Service:</strong> {quote.service}</p>
                <p><strong>Message:</strong><br/>{quote.message}</p>
            </div>
        </div>
        """
        _send_via_resend(
            to=settings.QUOTE_NOTIFY_EMAIL,
            subject=f"New Quote Request — {quote.service}",
            html=admin_html,
            text=body,
        )

        # ---- Email 2: Auto-reply to the client ----
        client_text = (
            f"Hi {quote.name},\n\n"
            f"Thank you for your interest in our services. We've received "
            f"your quote request for {quote.service} and our team will "
            f"review the details you've provided.\n\n"
            f"We look forward to getting in touch with you soon.\n"
            f"Best regards,\nLithavi International"
        )
        client_html = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <div style="background: #0a1e3f; padding: 24px;">
                <h1 style="color: #ffffff; margin: 0; font-size: 18px;">Lithavi International</h1>
            </div>
            <div style="padding: 32px; background: #ffffff; border: 1px solid #eee;">
                <p>Hi {quote.name},</p>
                <p>Thank you for your interest in our services. We've received
                your quote request for <strong>{quote.service}</strong> and our
                team will review the details you've provided.</p>
                <p>We look forward to getting in touch with you soon.</p>
                <p style="margin-top: 24px;">Best regards,<br/><strong>Lithavi International</strong></p>
            </div>
        </div>
        """
        _send_via_resend(
            to=quote.email,
            subject="Thank you for reaching out to Lithavi International",
            html=client_html,
            text=client_text,
        )

        quote.email_sent = True
        quote.save(update_fields=["email_sent"])
    except Exception as e:
        print(f"Failed to send quote email: {e}")


class QuoteRequestCreateView(APIView):
    def post(self, request):
        client_ip = _get_client_ip(request)
        cache_key = f"quote_rate_limit_{client_ip}"

        if cache.get(cache_key):
            return Response(
                {
                    "detail": "You've already submitted a request recently. "
                    "Please wait 15 minutes before submitting again."
                },
                status=status.HTTP_429_TOO_MANY_REQUESTS,
            )

        serializer = QuoteRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quote = serializer.save()

        cache.set(cache_key, True, RATE_LIMIT_SECONDS)

        # Send both emails on a background thread so this request doesn't
        # block on SMTP (which can be slow or blocked outbound on some
        # hosts, e.g. Railway) and cause the client-side fetch to time out.
        threading.Thread(
            target=_send_quote_emails, args=(quote.id,), daemon=True
        ).start()

        return Response(
            {"message": "Quote request received."},
            status=status.HTTP_201_CREATED,
        )