from CatApp.celery import celery
from CatApp.post_server import send_email


@celery.task
def sent_notification_change_password(user_email):
    subject = "🐱 LinkCat: service notification! ⚠️"
    message = "Your password was updated! 🗝️"
    send_email(user_email, subject, message)


@celery.task
def sent_greetings(user_email):
    subject = "🐱 LinkCat: Welcome!"
    message = "You registered successfully!"
    send_email(user_email, subject, message)


@celery.task
def sent_link_for_reset_password(user_email, link):
    subject = "🐱 LinkCat: reset password!"
    message = f"Follow it to reset password:\n{link}"
    send_email(user_email, subject, message)
