from django import forms
#from tasks.models import
from django.contrib.auth.models import Users

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text ="Please enter a username")
    first_name = forms.CharField(help_text ="Please enter your first name")
    last_name = forms.CharField(help_text = "Please enter you last name")
    email = forms.CharField(help_text = "Please enter your email")
    password = forms.CharField(widget = forms.PasswordInput(), help_text = "Please enter you password")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
