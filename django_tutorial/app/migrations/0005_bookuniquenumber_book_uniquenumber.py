# Generated by Django 4.2.1 on 2023-05-12 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_book_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookUniqueNumber",
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
                ("ISBN_10", models.CharField(blank=True, max_length=10, unique=True)),
                ("ISBN_13", models.CharField(blank=True, max_length=13, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="uniqueNumber",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.bookuniquenumber",
            ),
        ),
    ]
