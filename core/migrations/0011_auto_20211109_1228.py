# Generated by Django 2.2.13 on 2021-11-09 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20211109_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentrequestmodel',
            old_name='phone_number',
            new_name='mobile_number',
        ),
        migrations.RenameField(
            model_name='contentrequestmodel',
            old_name='full_name',
            new_name='names',
        ),
    ]
