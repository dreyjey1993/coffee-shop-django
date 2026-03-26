from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-Mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=200, label='Betreff', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Nachricht', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    captcha = CaptchaField(label='Bitte bestätige, dass du kein Roboter bist')