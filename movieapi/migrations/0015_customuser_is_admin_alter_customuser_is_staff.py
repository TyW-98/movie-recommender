# Generated by Django 4.2.1 on 2023-05-15 02:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movieapi", "0014_alter_movie_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
    ]
