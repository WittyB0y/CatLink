import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from CatApp import settings


def send_email(to_email, subject, message):  # Func for sent email
    from_email = settings.EMAIL_USER

    msg = MIMEMultipart()
    msg.attach(MIMEText(message, 'plain'))

    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # use context manager to open connection with Post Server
    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.starttls()
        server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
        server.sendmail(from_email, to_email, msg.as_string())
