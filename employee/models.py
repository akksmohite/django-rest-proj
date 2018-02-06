from __future__ import unicode_literals
from django.db import models
from company.models import Company


class Employee(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    designation = models.CharField(max_length=255)
    salary = models.DecimalField(decimal_places=2, max_digits=20)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
