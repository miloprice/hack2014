from django.db import models

class Task(models.Model):
    name = models.CharField()
    assigned = models.DateTimeField()
    due = models.DateTimeField()
    tags = models.CharField()
    priority = models.ForeignKey(Priority)
    status = models.ForeignKey(Status)
    size = models.ForeignKey(Size)
    all_day = models.BooleanField()
    repeat = models.BooleanField()
    location = models.CharField()
    desc = models.CharField()

class Priority(models.Model):
    name = models.CharField()
    ranking = models.IntegerField()

class Status(models.Model):
    completed = models.IntegerField()
    total = models.IntegerField()
    qualitative = models.CharField()

class Size(models.Model):
    name = models.CharField()
    ranking = models.IntegerField()
