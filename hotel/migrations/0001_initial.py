# Generated by Django 4.2 on 2023-07-26 19:36

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='Un nom par défaut', max_length=100)),
                ('description', models.TextField(blank=True, default='Une description par défaut')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('lieu', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('ifu', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('tel', models.CharField(default=None, max_length=20, null=True)),
                ('mail', models.EmailField(blank=True, default=None, max_length=254, unique=True)),
                ('site_web', models.URLField(blank=True, null=True)),
                ('adresse', models.CharField(blank=True, max_length=200, null=True)),
                ('pays', models.CharField(blank=True, max_length=100)),
                ('ville', models.CharField(blank=True, max_length=100)),
                ('code_postal', models.CharField(blank=True, max_length=10)),
                ('region', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
