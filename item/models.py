from __future__ import unicode_literals

from django.db import models
# from django.contrib.postgres.fields import ArrayField

class item(models.Model):
    """item"""
<<<<<<< HEAD
    item_id = models.IntegerField(default=0, primary_key=True)
=======
    id = models.IntegerField(default=0, primary_key=True)
>>>>>>> 75dd0da0c5446ad5269c80054de79fad7b804633
    deleted = models.BooleanField(default=False)
    TYPES = (('S', "story"), ('C', "comment"),)
    type = models.CharField(
        max_length=10,
        choices=TYPES,
    )
    by = models.CharField(max_length=10)
<<<<<<< HEAD
    time = models.IntegerField('date publised')
=======
    time = models.DateTimeField('date publised')
>>>>>>> 75dd0da0c5446ad5269c80054de79fad7b804633
    text = models.CharField(max_length=200)
    dead = models.BooleanField(default=False)
    parent = models.IntegerField(default=0)
    # kids = ArrayField(models.IntegerField(default=0), size=100)
    kids = models.CharField(max_length=200)
    url = models.URLField()
    score = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    # parts = ArrayField(models.IntegerField(default=0), size=100)
    parts = models.CharField(max_length=200)
    descendant = models.IntegerField(default=0)
