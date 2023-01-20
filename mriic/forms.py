from django import forms
from .models import Person,NewsLetter
class ContactForm(forms.ModelForm):
    class Meta:
        model=Person
        fields="__all__"

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control','rows':5}),
        }

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = "__all__"
        labels = {
            "email": ""
        }
        widgets = {
            'email':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Your Email'})
        }

#from django.forms import ModelForm---> for reference
#class ContactForm(ModelForm):
#from django import forms
#class ContactForm(forms.ModelForm):