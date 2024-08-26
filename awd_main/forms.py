from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    """Form to Create new User"""
    usable_password = None
    # The above code snippet helps to hide the password authentication field
    
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Password confirmation", strip=False, widget=forms.PasswordInput, required=True)
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') # this also controls the arrangement on the page!

    
    