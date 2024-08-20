from django.shortcuts import render
from django.http import HttpResponse
from dataentry.task import celery_test_task

# Create your views here.
def home(request):
    return render(request, 'home.html')


def celery_test(request):
    # we can use the task in celery_test_task function
    celery_test_task.delay()
    return HttpResponse("<h3>Function executed successfully</h3>")


    
