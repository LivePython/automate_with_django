import os
from django.conf import settings
from django.shortcuts import redirect, render
from .utils import check_csv_errors, get_all_custom_models
from uploads.models import Upload
from .task import import_data_task
# Now we can use the command in dataentry\management\commands python files using

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

        # check for csv error
        try:
            check_csv_errors(file_path, model_name)
        except Exception as d:
            messages.error(request, d)
            return redirect('import_data')

        # Handle the data importantion task using celery
        import_data_task.delay(file_path, model_name)
        messages.success(request, 'Your data is imported, you will get an email soon!')

        return redirect('import_data')

    else:
        custom_models = get_all_custom_models()
        
        context = {
            'custom_models': custom_models
        }
    return render(request, 'dataentry/importdata.html', context)
