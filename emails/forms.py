from django import forms
from .models import Email


class EMailForm(forms.ModelForm):
    # This is a way to make a form from a model 
    class Meta:
        model = Email
        fields = ('__all__')

