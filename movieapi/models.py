from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django_countries.fields import CountryField
from datetime import date

# Create your models here.
class Movie(models.Model):
    
    title = models.CharField(max_length=32, blank=False)
    genre = models.CharField(max_length=32, blank=False)    
    language = models.CharField(max_length=32, blank=False)
    release_year = models.IntegerField(blank=False)
    published_date = models.DateField(validators= [MaxValueValidator(date.today())], default=date.today())
    metascore = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)], blank = False)
    duration = models.BigIntegerField(blank = False)
    
    class Meta:
        verbose_name_plural = 'Movies'
        
class Director(models.Model):
    
    name = models.CharField(max_length=32)
    dob = models.DateField(validators = [MaxValueValidator(date.today())])
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='movie', null=True)
    
class Actor(models.Model):
    
    name = models.CharField(max_length=32, blank = False)
    dob = models.DateField(validators = [MaxValueValidator(date.today())])
    movies = models.ManyToManyField(Movie)

class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email, password, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **other_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username, email, password, **other_fields)
    
class CustomUser(AbstractUser, PermissionsMixin):
    
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('O', 'Other'),
    )
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=100, unique=True, null=True)
    preferred_name = models.CharField(max_length= 32, blank = True)
    age = models.IntegerField(validators =[MinValueValidator(0), MaxValueValidator(150)], default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    country = CountryField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
     
    class Meta: 
        unique_together = (('username', 'email'))
        
class RatedMovies(models.Model):
    
    movie = models.ForeignKey(Movie, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, blank=False, on_delete=models.CASCADE, related_name='ratedmovies')
    userRating = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)], blank=False)
    
    class Meta: 
        unique_together = (('user', 'movie'))
        index_together = (('user', 'movie'))
        
    
    

    
    

    