# The utils.py file is created to store utility functions
import csv
import hashlib
from bs4 import BeautifulSoup
import time
from django.core.mail import EmailMessage
import os
from django.core.management.base import CommandError
from django.apps import apps
from django.db import DataError 
 
from django.conf import settings

from datetime import datetime

from emails.models import Email, Sent, EmailTracking, Subsriber


def get_all_custom_models():
    # This function will help to get all the models that exist in the entire project
    default_models = ['ContentType', 'Session', 'LogEntry', 'Permission', 'Group', 'Upload', 'User']

    # get all the apps
    custom_models = []
    for model in apps.get_models():
        if model.__name__ not in default_models:
            custom_models.append(model.__name__)

    return custom_models


def check_csv_errors(file_path, model_name):
    # Search for the model across all installed apps 
    # This is done by looping through all the apps in the project
    model = None
    for app_config in apps.get_app_configs():
        # We search for the model

        try:
            model = apps.get_model(app_config.label, model_name)
            break 
        except LookupError:
            continue # keep searching next app

    if not model:
        raise CommandError(f'Model "{model_name}" not be found in any app')
    
    # we want to compare csv header with model field name
    # first get all the model field names
    model_field_names = [field.name for field in model._meta.fields][1:]
    
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            # getting header name of the csv
            csv_header = reader.fieldnames

            # compare csv header fieldnames with the model field name
            if csv_header != model_field_names:
                raise DataError(f"CSV file does not match {model_name} table fields")
            
    except Exception as e:
        raise e
    
    return model


def send_email_notification(subject, message, recipient_list, attachment=None, email_id=None):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        
        for recipient_email in recipient_list:
            new_message = message

            if email_id:
                email = Email.objects.get(pk=email_id)
                subscriber = Subsriber.objects.get(email_list=email.email_list, email_address=recipient_email)
                timestamp = str(time.time())
                data_to_hash = f'{recipient_email}{timestamp}'
                unique_id = hashlib.sha256(data_to_hash.encode()).hexdigest()

                email_tracking = EmailTracking.objects.create(
                    email=email,
                    Subsriber=subscriber,
                    unique_id=unique_id,

                )

                #  Create EmailTracking record
                # ngrok token; 2mmbl3QW8KdRDDfXjYQUpQszjGg_2ErnzxSfqqJouQaVgGCa1
                click_tracking_url = f'{settings.BASE_URL}/emails/track/click/{unique_id}'

                open_tracking_url = f'{settings.BASE_URL}/emails/track/open/{unique_id}'

                # Search for the links in the email body
                soup = BeautifulSoup(message, 'html.parser')
                urls = [item['href'] for item in soup.find_all('a', href=True)]


                # If there are links in the email body, inject our click tracking url to that link
                if urls:
                    for url in urls:
                        tracking_url = f"{click_tracking_url}?url={url}"
                        new_message = new_message.replace(url, tracking_url)
                
                else:
                    print('No URLs found in the email content')
                
                # Create email content with tracking pixel image
                open_tracking_img = f"<img src='{open_tracking_url}' width='1' height=1>"
                new_message += open_tracking_img

            email = EmailMessage(subject, new_message, from_email, to=recipient_list)
            
            if attachment is not None:
                email.attach_file(attachment)

            # Register in the code te html content
            email.content_subtype = 'html'
            email.send()

        # Store the total sent emails inside the Sent model
        if email_id:
            email_instance = Email.objects.get(pk=email_id)  # Fetch the Email model instance
            sent = Sent()
            sent.email = email_instance  # Use the model instance, not EmailMessage
            sent.total_sent = email_instance.email_list.count_emails()  # Use the model instance here
            sent.save()

    except Exception as g:
        raise g


def generate_csv_file(model_name):
    # Getting the timestamp
    export_dir = 'exported_data'
    timestamp = datetime.now().strftime("%d-%m-%Y")
    file_name = f'Exported_data_{model_name}_{timestamp}.csv'

    file_path = os.path.join(settings.MEDIA_ROOT, export_dir, file_name)
    return file_path

