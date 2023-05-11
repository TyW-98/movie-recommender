from django.db import models

# Create your models here.

class Book(models.Model):
    
    title = models.CharField(max_length=36)
    year = models.IntegerField(null=True)