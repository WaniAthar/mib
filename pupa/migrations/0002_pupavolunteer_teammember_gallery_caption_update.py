# Generated by Django 4.1.4 on 2022-12-14 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pupa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PupaVolunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='volunteer_avatars')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='team_avatars')),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='caption',
            field=models.TextField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=1500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
