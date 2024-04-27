# Generated by Django 5.0 on 2024-04-13 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BugReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("NEW", "Новая"),
                            ("IN_WORK", "В работе"),
                            ("COMPLETED", "Завершена"),
                        ],
                        default="NEW",
                        max_length=30,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("ZERO", "0"),
                            ("ONE", "1"),
                            ("TWO", "2"),
                            ("THREE", "3"),
                            ("FOUR", "4"),
                            ("FIVE", "5"),
                        ],
                        default="NULL",
                        max_length=5,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bug_reports",
                        to="tasks.project",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="bug_reports",
                        to="tasks.task",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeatureRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CONSIDERATION", "Рассмотрение"),
                            ("ACCEPTED", "Принято"),
                            ("REJECTED", "Отклонено"),
                        ],
                        default="CONSIDERATION",
                        max_length=30,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("ZERO", "0"),
                            ("ONE", "1"),
                            ("TWO", "2"),
                            ("THREE", "3"),
                            ("FOUR", "4"),
                            ("FIVE", "5"),
                        ],
                        default="NULL",
                        max_length=5,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feature_requests",
                        to="tasks.project",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="feature_requests",
                        to="tasks.task",
                    ),
                ),
            ],
        ),
    ]