from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Prints Hello world" # python manage.py hello --help

    # This function takes the logiic
    def handle(self, *args, **kwargs):
        # python manage.py hello
        self.stdout.write('Hello World')


