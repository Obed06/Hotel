# Generated by Django 4.2 on 2023-07-26 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifu', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('phone_number', models.CharField(default=None, max_length=20, null=True)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, unique=True)),
                ('speciality', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('years_of_experience', models.IntegerField(default=0, null=True)),
                ('grade', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('job_title', models.CharField(default='Cuisinier', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
