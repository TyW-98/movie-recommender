# Generated by Django 4.2.1 on 2023-05-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_bookuniquenumber_book_uniquenumber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookuniquenumber",
            name="ISBN_10",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="bookuniquenumber",
            name="ISBN_13",
            field=models.CharField(blank=True, max_length=13),
        ),
    ]
