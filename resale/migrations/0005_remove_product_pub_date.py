# Generated by Django 4.1.1 on 2023-05-22 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resale', '0004_product_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
    ]
