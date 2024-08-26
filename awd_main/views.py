from django.shortcuts import redirect, render
from django.http import HttpResponse
from dataentry.task import celery_test_task
from .forms import RegistrationForm # the registration form is gotten from here
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm # this is used to make the login form


# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Successful.')
            return redirect('register')
        
        else:
            context = {
                'form': form,
                }
            return render(request, 'register.html', context)
        
    else:
        form = RegistrationForm()
        
        context = {
            'form': form,
        }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        # This is where the login logic is handled 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('home')

            
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        form = AuthenticationForm()
        context = {'form': form} 
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')


def celery_test(request):
    # we can use the task in celery_test_task function
    celery_test_task.delay()
    return HttpResponse("<h3>Function executed successfully</h3>")


    
