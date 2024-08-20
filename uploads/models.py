from django.db import models

# Create your models here.
class Upload(models.Model):
    file = models.FileField(upload_to='uploads/') # This takes note of the files stored in the media\uploads directory
    # Triggered when a file gets to the directory
    model_name = models.CharField(max_length=50)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name
    
