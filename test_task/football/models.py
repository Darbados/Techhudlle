from __future__ import unicode_literals
from django.db import models


class Leagues(models.Model):
    id = models.AutoField(primary_key=True)
    league_title = models.CharField(default="", max_length=255)
    country = models.CharField(default="", max_length=100)
    added_at = models.DateTimeField('date created')

    class Meta:
        app_label = 'football'
        managed = False
        db_table = 'leagues'


class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default="", max_length=255)
    country = models.CharField(default="", max_length=100)
    created_at = models.DateTimeField('date created')

    class Meta:
        app_label = 'football'
        managed = False
        db_table = 'teams'


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default="", max_length=255)
    country = models.CharField(default="", max_length=100)
    start_time = models.DateTimeField()

    class Meta:
        app_label = 'football'
        managed = False
        db_table = 'events'