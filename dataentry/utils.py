# The utils.py file is created to store utility functions
import csv
from django.core.mail import EmailMessage
import os
from django.core.management.base import CommandError
from django.apps import apps
from django.db import DataError 
 
from django.conf import settings

from datetime import datetime

from emails.models import Email, Sent


def get_all_custom_models():
    # This function will help to get al the models that exist in the entire project
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
    from_email = settings.DEFAULT_FROM_EMAIL
    email = EmailMessage(subject, message, from_email, to=recipient_list)
    try:
        if attachment:
            email.attach_file(attachment)

        # Register in the code te html content
        email.content_subtype = 'html'
        email.send()

        # Store the total sent emails inside the Sent model
        email = Email.objects.get(pk=email_id)
        sent = Sent()
        sent.email = email
        sent.total_sent = email.email_list.count_emails()
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

