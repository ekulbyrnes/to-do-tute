from django import forms
from django.forms import ModelForm

from .models import *

class callsignForm(forms.ModelForm):
    
    class Meta:
        model = callsign
        fields = '__all__'