from django import forms
from .models import userdata

class Myform(forms.ModelForm):
    
    class Meta:
        model = userdata
        fields = ["first_name","last_name","father_name","about_you","profile"]

