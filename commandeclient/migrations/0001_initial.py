# Generated by Django 4.2 on 2023-08-16 18:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservation', '0001_initial'),
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandeClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commande', models.DateField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.reservation')),
                ('produits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produit.produit')),
            ],
        ),
        migrations.CreateModel(
            name='LigneCommandeClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('commande', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='commandeclient.commandeclient')),
            ],
        ),
    ]
