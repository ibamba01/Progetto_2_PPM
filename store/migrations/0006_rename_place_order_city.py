# Generated by Django 4.1 on 2023-06-04 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_order_orderitem"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="place",
            new_name="city",
        ),
    ]
