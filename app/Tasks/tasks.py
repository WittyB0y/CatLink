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
def sent_new_password(user_email, new_password):
    subject = "🐱 LinkCat: new password!"
    message = f"Hi!\nYour new password is {new_password}"
    send_email(user_email, subject, message)
