# Generated by Django 4.2 on 2023-07-26 19:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chambre', '0001_initial'),
        ('userprofile', '0001_initial'),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_service', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('fin_service', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('date_reservation', models.DateField(default=django.utils.timezone.now)),
                ('fin_reservation', models.DateField(default=django.utils.timezone.now)),
                ('is_available', models.BooleanField(blank=True, default=False)),
                ('is_valid', models.BooleanField(blank=True, default=False)),
                ('chambre', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='chambre.chambre')),
                ('services', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='service.service')),
                ('utilisateur', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile')),
            ],
        ),
    ]
