# The utils.py file is created to store utility functions
import csv
from email.message import EmailMessage
from django.core.management.base import CommandError

from django.apps import apps
from django.db import DataError 

from django.conf import settings


def get_all_custom_models():
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

def send_email(email_subject, email_message, to_email):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        mail = EmailMessage(email_subject, email_message, from_email, to=[to_email])
        mail.send()
    except Exception as e:
        raise e