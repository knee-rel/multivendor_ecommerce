# Generated by Django 4.2.16 on 2024-10-30 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0004_alter_product_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShippingTracking",
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
                ("tracking_number", models.CharField(max_length=50)),
                ("status", models.CharField(max_length=100, null=True)),
                ("shipped_date", models.DateTimeField(null=True)),
                ("delivery_date", models.DateTimeField(null=True)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.order",
                    ),
                ),
            ],
        ),
    ]
