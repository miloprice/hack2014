from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #basic user model
    def __unicode__(self):
        return self.user.name


