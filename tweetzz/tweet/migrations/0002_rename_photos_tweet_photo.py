# Generated by Django 5.0.7 on 2024-07-23 13:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tweet", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tweet",
            old_name="photos",
            new_name="photo",
        ),
    ]