from datetime import date

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False)
    released_year = models.IntegerField(default=date.today().year)
    genre = models.CharField(max_length=32, blank=False)
    language = models.CharField(max_length=32, default="-")
    duration = models.IntegerField(null=True)
    cast = models.ManyToManyField(Actor, related_name="movies")
    director = models.ForeignKey(
        Director, on_delete=models.SET_NULL, null=True, related_name="movies"
    )
    MPAA_rating = models.CharField(max_length=32, default="-")
    trailer_url = models.URLField(max_length=200)
    poster_image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.title + f" ({self.released_year})"


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        username,
        email,
        password,
        dob,
        display_name,
        gender,
        country,
        **other_fields,
    ):
        if not email:
            raise ValueError("Must provide an email")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            dob=dob,
            display_name=display_name,
            gender=gender,
            country=country,
            **other_fields,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(
        self,
        username,
        email,
        password,
        dob,
        display_name,
        gender,
        country,
        **other_fields,
    ):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("SuperUser must ahve is_superuser=True")

        return self.create_user(
            username,
            email,
            password,
            dob,
            display_name,
            gender,
            country,
            **other_fields,
        )


class CustomUser(AbstractUser, PermissionsMixin):
    GENDER_CHOICES = (("M", "male"), ("F", "female"), ("O", "other"))

    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=100, unique=True, null=False)
    display_name = models.CharField(max_length=32, blank=False, unique=True)
    dob = models.DateField(
        validators=[MaxValueValidator(timezone.localdate())],
        default=timezone.localdate(),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    country = models.CharField(max_length=200, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["email", "dob", "display_name", "gender", "country"]

    class Meta:
        unique_together = ("username", "email")

    def __str__(self):
        return self.display_name + f"({self.username})"


class RatedMovies(models.Model):
    movie = models.ForeignKey(Movie, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser, blank=False, on_delete=models.CASCADE, related_name="ratedmovies"
    )
    user_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], blank=False
    )

    class Meta:
        unique_together = ("user", "movie")
        index_together = ("user", "movie")

    def __str__(self):
        return f"{self.user.display_name} - {self.movie.title} ({self.user_rating})"
