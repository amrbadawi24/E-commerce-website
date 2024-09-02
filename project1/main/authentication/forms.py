from django import forms
from django.contrib.auth.forms import UserCreationForm , SetPasswordForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(error_messages={'required': 'Please enter a username'})
    password1 = forms.CharField(error_messages={'required': 'Please enter a password'})
    password2 = forms.CharField(error_messages={'required': 'Please confirm your password'})

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        
class UpdatepasswordrForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')