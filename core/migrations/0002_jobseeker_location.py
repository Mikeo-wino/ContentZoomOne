# Generated by Django 2.2.13 on 2021-10-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='Location',
            field=models.CharField(choices=[('EMB', 'Embakasi'), ('RAKS', 'Ruaraka'), ('MATH', 'Mathare')], default='RAKS', max_length=200),
        ),
    ]
