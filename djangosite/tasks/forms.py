from django import forms
from tasks.models import Size, Tag, Task, Subgoal
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget 
from django.contrib.admin.widgets import AdminDateWidget

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text = "Please enter a username")
    first_name = forms.CharField(help_text = "Please enter your first name")
    last_name = forms.CharField(help_text = "Please enter you last name")
    email = forms.CharField(help_text = "Please enter your email")
    password = forms.CharField(widget = forms.PasswordInput(), help_text = "Please enter you password")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class SizeForm(forms.ModelForm):

    class Meta:
        model = Size
        fields = ['name', 'ranking']

class TagForm(forms.ModelForm):
 
    class Meta:
        model = Tag
        fields = ['name', 'color']

class TaskForm(forms.ModelForm):
    name = forms.CharField(help_text = 'Name of task', label='Name')
    size = forms.ModelChoiceField(widget=forms.RadioSelect, empty_label = None, queryset = Size.objects.all(), help_text = 'Size')
    due = forms.DateField(widget = SelectDateWidget, help_text = 'Due date')
    all_day = forms.NullBooleanSelect()
    tags = forms.MultipleChoiceField(required=False, help_text = 'tags')
    desc = forms.CharField(help_text="Description of Task", required=False)
    location = forms.CharField(help_text="Location of Task", required=False)

    class Meta:
        model = Task
        fields = ['name', 'due', 'tags', 'size', 'all_day', 'repeat', 'location', 'desc']

class Subgoal(forms.ModelForm):

    class Meta:
        model = Subgoal
        fields = ['name', 'completed', 'task']
