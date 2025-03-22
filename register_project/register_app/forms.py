from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
class RegisterForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    def save(self):
        user = User.objects.create(
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            email=self.cleaned_data["email"],
            username=self.cleaned_data["username"],
            password=make_password(self.cleaned_data["password"])  
        )
        return user