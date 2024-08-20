from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Homapage'), # project homepage
    path('dataentry/', include('dataentry.urls')),
    path('celery-test/', views.celery_test),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this is the setting for having a media file saved in media folder
