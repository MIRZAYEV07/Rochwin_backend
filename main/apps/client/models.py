from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=255)
    birthdate = models.DateField()

