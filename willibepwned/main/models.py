from django.db import models

# Create your models here.
class smuck(models.Model):
    email = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
