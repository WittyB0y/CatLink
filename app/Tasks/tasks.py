import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from CatApp import settings
from CatApp.celery import celery


@celery.task
def sent_notification(user_email):
    from_email = settings.EMAIL_USER
    to_email = user_email

    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.starttls()
    server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
    msg = MIMEMultipart()

    message = "Your password was updated! 🗝️"
    msg.attach(MIMEText(message, "plain"))

    msg["Subject"] = "🐱 LinkCat: service notification! ⚠️"
    msg["From"] = from_email
    msg["To"] = to_email

    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()


@celery.task
def sent_greetings(user_email):
    from_email = settings.EMAIL_USER
    to_email = user_email

    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.starttls()
    server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
    msg = MIMEMultipart()

    message = "You registered successfully!"
    msg.attach(MIMEText(message, "plain"))

    msg["Subject"] = "🐱 LinkCat: Welcome!"
    msg["From"] = from_email
    msg["To"] = to_email

    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
