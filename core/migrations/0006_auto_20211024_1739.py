# Generated by Django 2.2.13 on 2021-10-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211024_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='full_name',
            field=models.CharField(default='Mike Ochieng', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='id_number',
            field=models.CharField(max_length=100),
        ),
    ]
