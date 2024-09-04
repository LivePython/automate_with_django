from django.shortcuts import redirect, render
from .forms import EMailForm
# import the messages from django
from django.contrib import messages
from dataentry.utils import send_email_notification
from django.conf import settings
from .models import Subsriber
from .task import sending_email_task

# Create your views here.

def send_email_attach(request):
    if request.method == 'POST':
        email_form = EMailForm(request.POST, request.FILES)
        
        if email_form.is_valid():
            email_form = email_form.save()
            # Send an email
            email_subject = request.POST.get('subject')
            email_message = request.POST.get('body')
            email_list = request.POST.get('email_list')
            
            # Lets access the selected email list 
            email_list = email_form.email_list
            
            # extract email addresses using email list in model
            subscribers = Subsriber.objects.filter(email_list=email_list)
            # Getting email list in the subscriber list
            to_email = [email.email_address for email in subscribers]
         

            if email_form.attachment:
                attachment = email_form.attachment.path # this takes care of the attachment
                
            else:
                attachment = None

            # celery handles the sending email functionalities
            sending_email_task.delay(email_subject, email_message, to_email, attachment)
            

            # Display a success message 
            messages.success(request, "Email Sent Successfully!")
            return redirect('send_email')

         
    else:
        email_form = EMailForm()
        context = {
            'email_form': email_form
        }
        return render(request, 'emails/send_email.html', context)
