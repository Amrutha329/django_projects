from django import forms
class ContactForm(forms.Form):
    username = forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput)
