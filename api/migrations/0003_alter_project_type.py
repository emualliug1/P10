# Generated by Django 4.1 on 2022-08-23 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="type",
            field=models.CharField(
                choices=[
                    ("backend", "Back-end"),
                    ("frontend", "Front-end"),
                    ("ios", "iOS"),
                    ("android", "Android"),
                ],
                max_length=15,
            ),
        ),
    ]
