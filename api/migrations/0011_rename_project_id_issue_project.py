# Generated by Django 4.1 on 2022-08-28 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_rename_author_id_comment_author_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="issue", old_name="project_id", new_name="project",
        ),
    ]
