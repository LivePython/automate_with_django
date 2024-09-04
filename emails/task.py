from awd_main.celery import app
from dataentry.utils import send_email_notification


@app.task
def sending_email_task(email_subject, email_message, to_email, attachment):
    
    send_email_notification(email_subject, email_message, to_email, attachment)
    return "Email sent successfully"