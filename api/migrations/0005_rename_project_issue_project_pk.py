# Generated by Django 4.1 on 2022-08-27 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_rename_author_comment_author_pk_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="issue", old_name="project", new_name="project_pk",
        ),
    ]
