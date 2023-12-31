# Generated by Django 4.1.9 on 2023-10-16 09:24

from django.db import migrations, models
import django_http_client.models.mixins
import django_http_client.utils


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Request",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "host",
                    models.CharField(
                        help_text="used for load balancing", max_length=255
                    ),
                ),
                ("url", models.CharField(max_length=255)),
                ("method", models.CharField(default="GET", max_length=255)),
                ("proxy", models.TextField(null=True)),
                ("data", models.TextField(null=True)),
                ("cookies", models.TextField(null=True)),
                ("headers", models.TextField(null=True)),
                ("allow_redirects", models.BooleanField(default=True)),
                ("disk_path", models.CharField(max_length=1024, null=True)),
                ("max_redirects", models.IntegerField(default=10, null=True)),
                ("max_retries", models.IntegerField(default=1, null=True)),
                ("retries_count", models.IntegerField(default=0, null=True)),
                ("verify_ssl", models.BooleanField(default=False, null=True)),
                ("timeout", models.IntegerField(null=True)),
                ("priority", models.IntegerField(default=0, null=True)),
                (
                    "created_at",
                    models.FloatField(
                        default=django_http_client.utils.get_timestamp, null=True
                    ),
                ),
                ("updated_at", models.FloatField(null=True)),
            ],
            options={
                "db_table": "http_client_request",
            },
            bases=(django_http_client.models.mixins.HeadersMixin, models.Model),
        ),
        migrations.CreateModel(
            name="RequestException",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("host", models.TextField()),
                ("url", models.TextField()),
                ("request_info", models.TextField()),
                ("exc_type", models.TextField()),
                ("exc_message", models.TextField()),
                ("timestamp", models.FloatField()),
            ],
            options={
                "db_table": "http_client_request_exception",
            },
            bases=(django_http_client.models.mixins.RequestInfoMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Response",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.CharField(max_length=255)),
                ("status", models.IntegerField()),
                ("headers", models.TextField(null=True)),
                ("request_info", models.TextField(null=True)),
                ("disk_path", models.CharField(max_length=1024, null=True)),
                (
                    "timestamp",
                    models.FloatField(default=django_http_client.utils.get_timestamp),
                ),
            ],
            options={
                "db_table": "http_client_response",
                "ordering": ("-timestamp",),
            },
            bases=(
                django_http_client.models.mixins.HeadersMixin,
                django_http_client.models.mixins.RequestInfoMixin,
                models.Model,
            ),
        ),
    ]
