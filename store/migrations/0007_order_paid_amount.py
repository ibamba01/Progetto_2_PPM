# Generated by Django 4.1 on 2023-06-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_rename_place_order_city"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="paid_amount",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
