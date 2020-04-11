from django import forms
from django.forms import ModelForm

from .models import demo
#SEND MAIL

class demo(ModelForm):
    class Meta:
        model = demo
        fields = ['business']
