from django import forms
from captcha.fields import CaptchaField

class PetitionForm(forms.Form):

    your_name = forms.CharField(label='Your name', widget= forms.TextInput(attrs={'class':'border-2 border-cblue rounded py-1'}))
    email = forms.CharField(label='Your email', widget= forms.TextInput(attrs={'class':'border-2 border-cblue rounded py-1'}))
    captcha = CaptchaField(label="Please enter the characters in the image")