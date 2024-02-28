from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64, null=True)
    year = models.IntegerField(null=True)
    ranking = models.DecimalField(max_digits=3, decimal_places=1, null=True)