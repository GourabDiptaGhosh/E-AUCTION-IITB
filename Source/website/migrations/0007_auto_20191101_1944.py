# Generated by Django 2.2.6 on 2019-11-01 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20191101_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='start_time',
            new_name='time_starting',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='start_time',
            new_name='time_starting',
        ),
    ]