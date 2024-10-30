# Generated by Django 4.2.16 on 2024-10-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0005_shippingtracking"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shippingtracking",
            name="status",
            field=models.CharField(
                choices=[
                    ("PND", "Pending"),
                    ("SHP", "Shipped"),
                    ("ITR", "In Transit"),
                    ("DLV", "Delivered"),
                    ("RTN", "Returned"),
                    ("CNL", "Cancelled"),
                ],
                default="PND",
                max_length=3,
            ),
        ),
    ]
