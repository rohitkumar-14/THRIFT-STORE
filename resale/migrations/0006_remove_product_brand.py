# Generated by Django 4.1.1 on 2023-05-22 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resale', '0005_remove_product_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
    ]
