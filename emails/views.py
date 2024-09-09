from django.shortcuts import redirect, render, get_object_or_404
from .forms import EMailForm
# import the messages from django
from django.contrib import messages
from dataentry.utils import send_email_notification
from django.conf import settings
from .models import Email, Subsriber, Sent
from .task import sending_email_task
from django.db.models import Sum

# Create your views here.

def send_email_attach(request):
    if request.method == 'POST':
        email_form = EMailForm(request.POST, request.FILES)
        
        if email_form.is_valid():
            email = email_form.save()
            # Send an email
            email_subject = request.POST.get('subject')
            email_message = request.POST.get('body')
            email_list = request.POST.get('email_list')
            
            # Lets access the selected email list 
            email_list = email.email_list
            
            # extract email addresses using email list in model
            subscribers = Subsriber.objects.filter(email_list=email_list)
            # Getting email list in the subscriber list
            to_email = [email.email_address for email in subscribers]
         

            if email.attachment:
                attachment = email.attachment.path # this takes care of the attachment
                
            else:
                attachment = None

            # celery handles the sending email functionalities
            email_id = email.id
            sending_email_task.delay(email_subject, email_message, to_email, attachment, email_id)
            

            # Display a success message 
            messages.success(request, "Email Sent Successfully!")
            return redirect('send_email')

         
    else:
        email = EMailForm()

        context = {
            'email_form': email
        }
        return render(request, 'emails/send_email.html', context)


def track_open(request):
    # Logic to store the open tracking information
    return

def track_click(request):
    # Logic to store the click tracking information
    return

def track_dashboard(request):
    emails = Email.objects.all().annotate(total_sent=Sum('sent__total_sent'))
    # The annotate function used above helps to introduce a new varible in model
    context = {
        'emails':emails,
    }
    return render(request, 'emails/track_dashboard.html', context)


def track_stats(request, pk):
    email = get_object_or_404(Email, pk=pk)
    sent = Sent.objects.get(email=email)
    context = {
        'email':email,
        'total_sent':sent.total_sent,
    }
    return render(request, 'emails/track_stats.html', context)
