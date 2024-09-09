from django.db import models
from ckeditor.fields import RichTextField #this is ckeditor package used for richtext feature usd in the body of the Email class


# Create your models here.

class List(models.Model):
    email_list = models.CharField(max_length=25)

    def __str__(self):
        return self.email_list
    
    def count_emails(self):
        count = Subsriber.objects.filter(email_list=self).count()
        return count
    

class Subsriber(models.Model):
    email_list = models.ForeignKey(List, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        return self.email_address
    

class Email(models.Model):
    email_list = models.ForeignKey(List, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    # body = models.TextField(max_length=5000) 
    # We ar not using the normal text field for the body. We are using the richtextfield here. Remember to add js scripts to the base.html

    body = RichTextField()

    attachment =models.FileField(upload_to='email_attachements/', blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    

class EmailTracking(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE, null=True, blank=True)
    Subsriber = models.ForeignKey(Subsriber, on_delete=models.CASCADE, null=True, blank=True)
    unique_id = models.CharField(max_length=255, unique=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    clicked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email.subject
    


class Sent(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE, null=True, blank=True)
    total_sent = models.IntegerField()

    def __str__(self):
        return f'{self.email} - {self.total_sent} emails sent'