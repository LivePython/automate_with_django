from django.core.management.base import BaseCommand, CommandError
from django.db import DataError
from dataentry.models import Student
from django.apps import apps
from dataentry.utils import check_csv_errors
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

        model = check_csv_errors(file_path, model_name)

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            for data in reader:
                model.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("Data imported from csv successfully!"))

