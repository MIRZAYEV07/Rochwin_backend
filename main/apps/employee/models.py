from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    birthdate = models.DateField()
