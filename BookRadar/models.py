from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64, null=True)
    year = models.IntegerField(null=True)
    ranking = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

