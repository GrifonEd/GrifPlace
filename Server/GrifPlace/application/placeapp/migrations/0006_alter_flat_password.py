# Generated by Django 4.1.2 on 2022-10-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeapp', '0005_flat_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='Password',
            field=models.CharField(max_length=12),
        ),
    ]