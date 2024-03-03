from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def email_sender(subject, template_name, reciver, context):
    html_file = render_to_string(template_name, context)
    message = strip_tags(html_file)
    send_mail(subject, message, settings.EMAIL_HOST_USER, [reciver], html_message=html_file)