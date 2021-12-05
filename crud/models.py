from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=40)
    salary = models.FloatField()
