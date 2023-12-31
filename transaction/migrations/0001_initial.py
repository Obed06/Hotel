# Generated by Django 4.2 on 2023-08-25 14:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compte', '0001_initial'),
        ('commandeclient', '0001_initial'),
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_transaction', models.DateField(default=django.utils.timezone.now)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('compte', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='compte.compte')),
                ('lignecommandeclient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commandeclient.lignecommandeclient')),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.reservation')),
            ],
        ),
    ]
