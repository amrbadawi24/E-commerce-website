from django import forms
from .models import *

class shippingform(forms.ModelForm):
    
    class Meta:
        model = shippingaddress
        fields = ("full_name","address1","phone_number","country","state","city")
        
class paymentform(forms.Form):
    card_name = forms.CharField(label="Card Name", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name on card'}),required=True)
    card_number = forms.CharField(label="Card Number", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'numbere of card'}),required=True)
    card_cvv =forms.CharField(label="Card PIN", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'PIN CODE'}),required=True)
    card_adddress1 = forms.CharField(label="Card address", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address of card owner'}),required=True)
    