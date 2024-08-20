from awd_main.celery import app
import time 
from django.core.management import call_command
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import send_email



@app.task
def celery_test_task():
    
    time.sleep(10)
    return 'Task completed successffully'

@app.task
def import_data_task(file_path:str, model_name:str):
    # trigger inportdata coomand
    try:
        # this helps us to use the commands created earlier

        # call_command('importdata', file_path, model_name)
        call_command('importdata', file_path, model_name)

    except Exception as e:
        raise e
    
    # send the user an email to notify task completion
    subject= 'Data successful'
    message = 'Your data is successfully imported'
    to_email = settings.DEFAULT_TO_EMAIL
    
    send_email(subject, message, to_email)
    
    return 'Data imported successfully!'
