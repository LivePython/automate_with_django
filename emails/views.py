from django.shortcuts import redirect, render
from .forms import EMailForm
# import the messages from django
from django.contrib import messages
from dataentry.utils import send_email_attachment
from django.conf import settings

# Create your views here.

def send_email(request):
    if request.method == 'POST':
        email_form = EMailForm(request.POST, request.FILES)
        
        if email_form.is_valid():
            email_form.save()
            # Send an email
            email_subject = request.POST.get('subject')
            email_message = request.POST.get('body')
            to_email = settings.DEFAULT_TO_EMAIL
            send_email_attachment(email_subject, email_message, to_email)

            # Display a success message 
            messages.success(request, "Email Sent Successfully!")
            return redirect('send_email')

         
    else:
        email_form = EMailForm()
        context = {
            'email_form': email_form
        }
        return render(request, 'emails/send_email.html', context)
