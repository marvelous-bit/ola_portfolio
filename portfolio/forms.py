from django import forms
from django.forms import ModelForm
from .models import ContactModel


class CONTACTFORM(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'subject','email', 'messagess')
        exclude = ['created']
        widgets={
            'name': forms.TextInput(attrs={'class':"form-control"}),
            'subject': forms.TextInput(attrs={'class':"form-control"}),
            'email': forms.TextInput(attrs={'class':"form-control"}),
            'messagess': forms.TextInput(attrs={'class':"form-control"}),
            
        }

