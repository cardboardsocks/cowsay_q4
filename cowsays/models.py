from django.db import models

# Create your models here.

class Cowsays(models.Model):
    cowsays = models.TextField(max_length=80)