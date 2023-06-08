from .models import *
from django.forms import ModelForm, TextInput


class UriForm(ModelForm):
    class Meta:
        model = Uri
        fields = ['uri']
        widgets = {'uri': TextInput(attrs={
            'class': 'form-control',
            'uri': 'uri',
            'id': 'uri',
        })}
