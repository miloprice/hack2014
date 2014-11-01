from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #basic user model
    def __unicode__(self):
        return self.user.name

class Priority(models.Model):
    name = models.CharField(max_length=32)
    ranking = models.IntegerField()
\
    def __unicode__(self):
        return self.name

class Status(models.Model):
    completed = models.IntegerField()
    total = models.IntegerField()
    qualitative = models.CharField(max_length=32)

class Size(models.Model):
    name = models.CharField(max_length=32)
    ranking = models.IntegerField()

class Tag(models.Model):
    name = models.CharField(max_length=32)

class Task(models.Model):
    name = models.CharField(max_length=32)
    assigned = models.DateTimeField()
    due = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    priority = models.ForeignKey(Priority)
    status = models.ForeignKey(Status)
    size = models.ForeignKey(Size)
    all_day = models.BooleanField(default=False)
    repeat = models.BooleanField(default=False)
    location = models.CharField(max_length=64)
    desc = models.CharField(max_length=128)
