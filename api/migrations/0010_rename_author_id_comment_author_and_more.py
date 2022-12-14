# Generated by Django 4.1 on 2022-08-28 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_rename_author_pk_comment_author_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="author_id", new_name="author",
        ),
        migrations.RenameField(
            model_name="comment", old_name="issue_id", new_name="issue",
        ),
        migrations.RenameField(
            model_name="contributor", old_name="project_id", new_name="project",
        ),
        migrations.RenameField(
            model_name="contributor", old_name="user_id", new_name="user",
        ),
        migrations.RenameField(
            model_name="issue", old_name="assignee_id", new_name="assignee",
        ),
        migrations.RenameField(
            model_name="issue", old_name="author_id", new_name="author",
        ),
    ]
