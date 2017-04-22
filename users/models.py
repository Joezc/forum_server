from __future__ import unicode_literals

from django.db import models

class user(models.Model):
    """user"""
    id = models.CharField(max_length=20, primary_key=True)
    delay = models.IntegerField(default=0)
    created = models.CharField(max_length=20)
    karma = models.IntegerField(default=0)
    about = models.CharField(max_length=20)
    submitted = models.CharField(max_length=200)
