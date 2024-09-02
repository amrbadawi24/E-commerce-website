from django import forms
from .models import comments,product

class commentForm(forms.ModelForm):
    
    class Meta:
        model = comments
        fields = ("body",)