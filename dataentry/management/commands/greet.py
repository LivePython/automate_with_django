from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Greeting users'

    def add_arguments(self, parser):
        # This allows taken a command in our arguments
        parser.add_argument('name', type=str, help='specifies user name')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greetings = f'Hi {name}, good morning'
        self.stdout.write(greetings) 
        # We can make the above expression an error type 
        #  by using the stderr.write() command as shwon below 
        #  self stderr.write(greetings)
        #  we can aslo style an output as shown below 
        self.stdout.write(self.style.SUCCESS(greetings))
        self.stdout.write(self.style.WARNING(greetings))
        self.stdout.write(self.style.ERROR(greetings))