from django.contrib import admin
from .models import List, Subsriber, Email

# Register your models here.
admin.site.register(List)
admin.site.register(Subsriber)
admin.site.register(Email)