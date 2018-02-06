from __future__ import unicode_literals
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)