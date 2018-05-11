from django.db import models

# Create your models here.

class Leagues(models.Model):
    title = models.CharField(default="", max_length=255)
    country = models.CharField(default="", max_length=100)
    created_at = models.DateTimeField('date created')

    class Meta:
        app_label = 'football'


