# Generated by Django 4.2.1 on 2023-05-13 04:17

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("movieapi", "0007_remove_movie_directed_by_movie_director"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="actor",
            name="moviesList",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="actorList",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="director",
        ),
        migrations.AddField(
            model_name="actor",
            name="movies",
            field=models.ManyToManyField(to="movieapi.movie"),
        ),
        migrations.AddField(
            model_name="director",
            name="movie",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="movie",
                to="movieapi.movie",
            ),
        ),
        migrations.AlterField(
            model_name="actor",
            name="dob",
            field=models.DateField(
                validators=[
                    django.core.validators.MaxValueValidator(datetime.date(2023, 5, 13))
                ]
            ),
        ),
        migrations.AlterField(
            model_name="director",
            name="dob",
            field=models.DateField(
                validators=[
                    django.core.validators.MaxValueValidator(datetime.date(2023, 5, 13))
                ]
            ),
        ),
    ]
