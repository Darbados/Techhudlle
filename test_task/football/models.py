from __future__ import unicode_literals
from django.db import models


class Leagues(models.Model):
    id = models.AutoField(primary_key=True)
    league_title = models.CharField(default="", max_length=255)
    country = models.CharField(default="", max_length=100)
    added_at = models.DateTimeField('date created')

    def __str__(self):
        return self.league_title

    class Meta:
        app_label = 'football'
        managed = False
        db_table = 'leagues'


class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default="", max_length=255)
    country = models.CharField(default="", max_length=100)
    league = models.CharField(default="", max_length=255)
    created_at = models.DateTimeField('date created')

    def __str__(self):
        return "{0} from {1}".format(self.title, self.league)

    class Meta:
        app_label = 'football'
        managed = False
        db_table = 'teams'


class EventsPremach(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default="", max_length=255)
    country = models.CharField(default="", max_length=100)
    status = models.CharField(default="", max_length=15)
    start_time = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'football'
        managed = False
        db_table = 'events_prematch'


class EventsLive(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default="", max_length=255)
    country = models.CharField(default="", max_length=100)
    status = models.CharField(default="", max_length=15)
    live_minute = models.CharField(default="", max_length=15)
    live_score_home = models.IntegerField(default=0)
    live_score_away = models.IntegerField(default=0)
    created_at = models.DateTimeField('date created')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'football'
        managed = False
        db_table = 'events_live'


class EventsFinished(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default="", max_length=255)
    country = models.CharField(default="", max_length=100)
    status = models.CharField(default="", max_length=15)
    start_time = models.DateTimeField()
    final_score_home = models.IntegerField(default=0)
    final_score_away = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'football'
        managed = False
        db_table = 'events_finished'