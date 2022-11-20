from django import forms
from .models import BASIC_DATA

class Myform(forms.ModelForm):
    
    class Meta:
        model = BASIC_DATA
        fields = ["first_name","last_name","father_name","mother_name","about_you","profile"]

