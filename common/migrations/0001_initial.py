# Generated by Django 5.0.6 on 2024-06-06 18:37

import common.models
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("code", models.CharField(max_length=20)),
                ("phone_code", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "verbose_name_plural": "Countries",
            },
        ),
        migrations.CreateModel(
            name="DocumentType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, unique=True)),
                ("code", models.CharField(max_length=20, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ghana_card",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=common.models.user_directory_path,
                    ),
                ),
                (
                    "passport_pic",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=common.models.user_directory_path,
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="common.country"
                    ),
                ),
                (
                    "document_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.documenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
