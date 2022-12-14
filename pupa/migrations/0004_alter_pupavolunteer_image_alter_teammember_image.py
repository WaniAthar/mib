# Generated by Django 4.1.4 on 2022-12-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupa', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupavolunteer',
            name='image',
            field=models.ImageField(blank=True, upload_to='volunteer_avatars'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.ImageField(blank=True, upload_to='team_avatars'),
        ),
    ]
