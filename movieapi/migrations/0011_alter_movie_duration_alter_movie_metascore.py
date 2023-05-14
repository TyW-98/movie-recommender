# Generated by Django 4.2.1 on 2023-05-14 22:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movieapi", "0010_remove_movie_release_year_alter_actor_dob_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="metascore",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
