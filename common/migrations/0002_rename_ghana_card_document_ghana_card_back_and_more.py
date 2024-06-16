# Generated by Django 5.0.6 on 2024-06-10 07:02

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="document",
            old_name="ghana_card",
            new_name="ghana_card_back",
        ),
        migrations.AddField(
            model_name="document",
            name="ghana_card_front",
            field=models.FileField(
                blank=True, null=True, upload_to=common.models.user_directory_path
            ),
        ),
    ]