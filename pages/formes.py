from dataclasses import fields
from django import forms
from .models import Logen


class FormLogen (forms.ModelForm):
    class Meta : 
        model = Logen
        fields = '__all__'