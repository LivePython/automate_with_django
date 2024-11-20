from django.contrib import admin
from .models import List, Subsriber, Email, EmailTracking, Sent

class EmailTrackingAdmin(admin.ModelAdmin):
    list_display = ['email', 'Subsriber', 'opened_at', 'clicked_at']


# Register your models here.
admin.site.register(List)
admin.site.register(Subsriber)
admin.site.register(Email)
admin.site.register(EmailTracking, EmailTrackingAdmin)
admin.site.register(Sent)
