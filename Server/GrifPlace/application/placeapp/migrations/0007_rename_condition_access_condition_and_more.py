# Generated by Django 4.1.2 on 2022-11-05 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placeapp', '0006_alter_flat_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='access',
            old_name='Condition',
            new_name='condition',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='ID_flat',
            new_name='flat_id',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='ID_access',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='Number_pasport',
            new_name='passport_number',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='Reason',
            new_name='reason',
        ),
        migrations.RenameField(
            model_name='flat',
            old_name='Area',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='flat',
            old_name='ID_flat',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='flat',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='flat',
            old_name='Type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='Number_pasport',
            new_name='passport_number',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='Phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='Second_name',
            new_name='second_name',
        ),
    ]
