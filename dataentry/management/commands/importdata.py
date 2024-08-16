from django.core.management.base import BaseCommand, CommandError
from django.db import DataError
from dataentry.models import Student
from django.apps import apps
import csv

# Propose command:  python manage.py importdata file_path


class Command(BaseCommand):
    help = 'import data from CSV file'

    def add_arguments(self, parser):
        # This allows taken a command in our arguments
        parser.add_argument('file_path', type=str, help='Add csv file path')
        parser.add_argument('model_name', type=str, help='Add model name')

    def handle(self, *args, **kwargs):
        # We add the function logic here
        # file path is C:\Users\DELL\Desktop\django\student_data.csv
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

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
        print(model_field_names)
        


        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            # getting header name of the csv
            csv_header = reader.fieldnames

            # compare csv header fieldnames with the model field name
            if csv_header != model_field_names:
                raise DataError(f"CSV file does not match {model_name} table fields")
            
            for data in reader:
                model.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("Data imported from csv successfully!"))

