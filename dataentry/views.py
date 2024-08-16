import os
from django.conf import settings
from django.shortcuts import redirect, render
from .utils import get_all_custom_models
from uploads.models import Upload
# Now we can use the command in dataentry\management\commands python files using
from django.core.management import call_command
# import the messages from django
from django.contrib import messages

# Create your views here.
def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')

        # lets record the uploaded file in uplods
        upload = Upload.objects.create(file=file_path, model_name=model_name)

        # construct the full path
        # relative_path = str(upload.file.url)
        # full_path = str(settings.BASE_DIR)
        # file_absolute_path = upload.file.path

        file_path = upload.file.path
        
        # trigger inportdata coomand
        try:
            # this helps us to use the commands created earlier
            call_command('importdata', file_path, model_name)

            # Compose the alert messages
            messages.success(request, 'Data imported successfully!')
        except Exception as e:

            messages.error(request, e)
            

        return redirect('import_data')



    else:
        custom_models = get_all_custom_models()
        
        context = {
            'custom_models': custom_models
        }
    return render(request, 'dataentry/importdata.html', context)
