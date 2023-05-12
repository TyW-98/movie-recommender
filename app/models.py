from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
    
    title = models.CharField(max_length=36, blank=False, unique=True)
    published_date = models.DateField(null=True)
    description = models.TextField(max_length=256, blank=True,)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    stock = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True, null=True)
    images = models.ImageField(upload_to="images/", blank=True)