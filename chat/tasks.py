from celery import shared_task
from django.core.mail import send_mail
from support.settings import EMAIL_HOST_USER


@shared_task
def status_update_notification(title, email, new_status):
    subject = 'Ticket updated'
    message = f'Status of your ticket "{title}" has changed to "{new_status}"'
    recepient = email
    send_mail(subject, message, EMAIL_HOST_USER,
              [recepient], fail_silently=False)
