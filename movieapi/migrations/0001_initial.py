# Generated by Django 4.2.1 on 2023-05-13 02:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("username", models.CharField(max_length=150, unique=True)),
                ("email", models.EmailField(max_length=100, null=True, unique=True)),
                ("preferred_name", models.CharField(blank=True, max_length=32)),
                (
                    "age",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(150),
                        ],
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(blank=True, max_length=2),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "unique_together": {("username", "email")},
            },
        ),
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                (
                    "dob",
                    models.DateField(
                        validators=[django.core.validators.MaxValueValidator(2023)]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Director",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                (
                    "dob",
                    models.DateField(
                        validators=[django.core.validators.MaxValueValidator(2023)]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32)),
                ("genre", models.CharField(max_length=32)),
                ("language", models.CharField(max_length=32)),
                ("release_year", models.IntegerField()),
                (
                    "metascore",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ]
                    ),
                ),
                ("duration", models.BigIntegerField()),
                (
                    "actorList",
                    models.ManyToManyField(related_name="movies", to="movieapi.actor"),
                ),
                (
                    "director",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="director",
                        to="movieapi.director",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Movies",
            },
        ),
        migrations.AddField(
            model_name="actor",
            name="moviesList",
            field=models.ManyToManyField(related_name="actors", to="movieapi.movie"),
        ),
        migrations.CreateModel(
            name="RatedMovies",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "userRating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ]
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movieapi.movie"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ratedmovies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "movie")},
                "index_together": {("user", "movie")},
            },
        ),
    ]
