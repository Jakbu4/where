from django.db import models
from datetime import datetime
# Create your models here.

class Place(models.Model):
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=50, default='')
    rate = models.FloatField(default=0.0)
    add_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title
    