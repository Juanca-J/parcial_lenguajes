from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario",
                               widget=forms.TextInput(attrs= {"placeholder":"Iniciando session"}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs= {"placeholder":"Password"}))


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "full_name", "email", "password1", "password2"]
