from datetime import date

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=32, blank=False)
    dob = models.DateField(
        validators=[MaxValueValidator(date.today())], default=date.today()
    )

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=32)
    dob = models.DateField(
        validators=[MaxValueValidator(date.today())], default=date.today()
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=32, blank=False)
    genre = models.CharField(max_length=32, blank=False)
    language = models.CharField(max_length=32, blank=False)
    published_date = models.DateField(
        validators=[MaxValueValidator(date.today())], default=date.today()
    )
    metascore = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        blank=False,
        default=0,
    )
    duration = models.IntegerField(null=True)
    actors = models.ManyToManyField(Actor, related_name="movies")
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE, null=True, related_name="movies"
    )

    def __str__(self):
        return self.title + f"({self.id})"
    
    def average_rating(self):
        ratings = RatedMovies.objects.filter(movie=self)
        total_rating = sum(rating.user_rating for rating in ratings)
        
        if len(ratings) > 0:
            average_rating = total_rating / len(ratings)
        else:
            average_rating = "Not Rated"
        
        return average_rating

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
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **other_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=100, unique=True, null=True)
    preferred_name = models.CharField(max_length=32, blank=True)
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(150)], default=0
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    country = CountryField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"

    class Meta:
        unique_together = ("username", "email")

    def __str__(self):
        return self.username + f"({self.id})"


class RatedMovies(models.Model):
    movie = models.ForeignKey(Movie, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser, blank=False, on_delete=models.CASCADE, related_name="ratedmovies"
    )
    user_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)], blank=False
    )

    class Meta:
        unique_together = ("user", "movie")
        index_together = ("user", "movie")

    def __str__(self):
        return str(self.movie.title) + f"({self.user.id})"
