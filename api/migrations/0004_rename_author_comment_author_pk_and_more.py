# Generated by Django 4.1 on 2022-08-27 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_project_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="author", new_name="author_pk",
        ),
        migrations.RenameField(
            model_name="comment", old_name="issue", new_name="issue_pk",
        ),
        migrations.RenameField(
            model_name="contributor", old_name="project", new_name="project_pk",
        ),
        migrations.RenameField(
            model_name="contributor", old_name="user", new_name="user_pk",
        ),
        migrations.RenameField(
            model_name="issue", old_name="assignee", new_name="assignee_pk",
        ),
        migrations.RenameField(
            model_name="issue", old_name="author", new_name="author_pk",
        ),
    ]