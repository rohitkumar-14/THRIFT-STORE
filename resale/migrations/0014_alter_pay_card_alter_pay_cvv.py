# Generated by Django 4.1.1 on 2023-05-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resale', '0013_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='card',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pay',
            name='cvv',
            field=models.IntegerField(),
        ),
    ]
