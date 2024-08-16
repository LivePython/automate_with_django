import csv
from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student, Customer
from django.apps import apps 
import datetime 

class Command(BaseCommand):
    help = 'Export data from database model to csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Enter the csv file path')
        parser.add_argument('model_name', type=str, help='Enter the model name')
            

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        # Now we search for the model
        model = None
        for app in apps.get_app_configs():
            try:
                model = apps.get_model(app.label, model_name)
                break
            except LookupError:
                 continue
        

        if not model:
             raise CommandError(f'No model named {model_name}')
        else:
             data = model.objects.all()
        
        # Getting the timestamp
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y")
        file_path = f'{file_path}_{timestamp}.csv'
        
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            # write the CSV header
            # ['Roll num', 'Name', 'Age']
            writer.writerow([field.name for field in model._meta.fields])

            # write data rows
            for dat in data:
                writer.writerow([getattr(dat, field.name) for field in model._meta.fields])
        

        self.stdout.write(self.style.SUCCESS("Data exported successfully!"))
            

    

