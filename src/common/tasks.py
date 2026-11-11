import smtplib

from celery import shared_task
from django.core.mail import send_mail


@shared_task(
    name="common.tasks.send_email",
    ignore_result=False,
    autoretry_for=(smtplib.SMTPException, OSError),
    retry_backoff=True,
    retry_backoff_max=300,
    retry_jitter=True,
    max_retries=5,
)
def send_email_task(
    subject: str,
    message: str,
    recipient_list: list[str],
    from_email: str | None = None,
    html_message: str | None = None,
) -> int:
    if not recipient_list:
        raise ValueError("At least one email recipient is required.")

    return send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False,
        html_message=html_message,
    )