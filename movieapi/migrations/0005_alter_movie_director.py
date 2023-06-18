# Generated by Django 4.2.1 on 2023-05-13 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("movieapi", "0004_alter_movie_actorlist_alter_movie_director"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="director",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="director",
                to="movieapi.director",
            ),
        ),
    ]