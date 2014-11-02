from django import forms
from tasks.models import Priority, Status, Size, Tag, Task, Subgoal
from django.contrib.auth.models import Users

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text = "Please enter a username")
    first_name = forms.CharField(help_text = "Please enter your first name")
    last_name = forms.CharField(help_text = "Please enter you last name")
    email = forms.CharField(help_text = "Please enter your email")
    password = forms.CharField(widget = forms.PasswordInput(), help_text = "Please enter you password")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ['qualitative']

class SizeForm(forms.ModelForm):

    class Meta:
        model = Size
        fields = ['name', 'ranking']

class TagForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = ['name', 'color']

class Task(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'assigned', 'due', 'tags', 'status', 'size', 'all_day', 'repeat', 'location', 'desc']

class Subgoal(forms.ModelForm):

    class Meta:
        model = Subgoal
        fields = ['name', 'completed', 'task']
