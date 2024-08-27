from django.db import models

# Create your models here.

class List(models.Model):
    email_list = models.CharField(max_length=25)

    def __str__(self):
        return self.email_list
    

class Subsriber(models.Model):
    email_list = models.ForeignKey(List, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        return self.email_address
    

class Email(models.Model):
    email_list = models.ForeignKey(List, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    body = models.TextField(max_length=5000)
    attachment =models.FileField(upload_to='email_attachements/', blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    