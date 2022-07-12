from typing_extensions import Required
from django.db import models
from django import forms

class Project(models.Model):
    name = models.CharField(max_length=50)
    organization_name = models.CharField(max_length=70)
    technology = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    bug_count=models.IntegerField()

    def __str__(self):
        return self.name