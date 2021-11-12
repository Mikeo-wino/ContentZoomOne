# Generated by Django 2.2.13 on 2021-10-24 14:35

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211024_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='Last_name',
        ),
        migrations.RemoveField(
            model_name='jobseeker',
            name='first_name',
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='company',
            field=models.CharField(default='orange points', max_length=100),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='full_name',
            field=models.CharField(default='Mike Ochieng', max_length=50),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='terms',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
