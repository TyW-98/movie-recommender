from django.db import models
import uuid

# Create your models here.

class BookUniqueNumber(models.Model):
    
    ISBN_10 = models.CharField(max_length = 10, blank=True)
    ISBN_13 = models.CharField(max_length = 13, blank=True)

class Book(models.Model):
    
    title = models.CharField(max_length=36, blank=False, unique=True)
    published_date = models.DateField(null=True)
    description = models.TextField(max_length=256, blank=True,)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    stock = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True, null=True)
    images = models.ImageField(upload_to="images/", blank=True)
    
    uniqueNumber = models.OneToOneField(BookUniqueNumber, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + "-" + str(self.id)
    
class Character(models.Model):
    
    name = models.CharField(max_length = 100, blank=True)
    book = models.ForeignKey(Book, blank=True, on_delete=models.SET_NULL, null=True, related_name='characters')