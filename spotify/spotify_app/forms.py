from .models import *
from django.forms import ModelForm, TextInput
from django import forms

class UriForm(forms.ModelForm):
    class Meta:
        model = Uri
        fields = ['uri']
        widgets = {'uri': forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'uri',
        })}