# Generated by Django 4.2.1 on 2023-05-14 22:07

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movieapi", "0009_remove_actor_movies_remove_director_movie_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="release_year",
        ),
        migrations.AlterField(
            model_name="actor",
            name="dob",
            field=models.DateField(
                default=datetime.date(2023, 5, 14),
                validators=[
                    django.core.validators.MaxValueValidator(datetime.date(2023, 5, 14))
                ],
            ),
        ),
        migrations.AlterField(
            model_name="director",
            name="dob",
            field=models.DateField(
                default=datetime.date(2023, 5, 14),
                validators=[
                    django.core.validators.MaxValueValidator(datetime.date(2023, 5, 14))
                ],
            ),
        ),
    ]
