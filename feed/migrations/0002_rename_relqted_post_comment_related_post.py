# Generated by Django 4.1 on 2024-01-18 22:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("feed", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="relqted_post",
            new_name="related_post",
        ),
    ]
