from django import forms
from .models import *

class Normal_form(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()
    place=forms.CharField()

class Model_Form(forms.ModelForm):
    class meta:
        model=Project_user
        fields='_all_' 
