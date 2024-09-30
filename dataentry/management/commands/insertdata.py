from django.core.management.base import BaseCommand
from dataentry.models import Student


# I want to add some data to the database using the custom command

class Command(BaseCommand):
    help = 'Insert data to database'

    def handle(self, *args, **kwargs):
        data_set = [
            {'roll_num': 1002, 'name':'Solomon', 'age':23},
            {'roll_num': 1003, 'name':'Adeoye', 'age':28},
            {'roll_num': 1004, 'name':'Michael', 'age':33},
            {'roll_num': 1005, 'name':'Charles', 'age':36},
            {'roll_num': 1006, 'name':'Ben', 'age':27}
        ]

        # Student.objects.create(roll_num=1001, name='Teejay', age=29)
        for data in data_set:
            # checking for data availability before storing
            roll_num = data['roll_num']
            existing_data = Student.objects.filter(roll_num=roll_num).exists() # This will return true or false
            if not existing_data:
                Student.objects.create(roll_num=data['roll_num'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f"Data with roll num {roll_num} already exits in database!"))
                 

        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))
