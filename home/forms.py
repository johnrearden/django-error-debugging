from django.forms import ModelForm
from django import forms
from .models import Person


class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
        widgets={
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                
            }),
        }