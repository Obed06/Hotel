# Generated by Django 4.2 on 2023-08-14 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, unique=True)),
                ('nom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile')),
            ],
        ),
    ]
