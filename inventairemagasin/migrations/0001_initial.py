# Generated by Django 4.2 on 2023-08-16 18:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventaireMagasin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('produits', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produit.produit')),
            ],
        ),
        migrations.CreateModel(
            name='LigneInventaireMagasin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite_reel', models.IntegerField(default=0)),
                ('quantite_virtuel', models.IntegerField(default=0)),
                ('motif', models.CharField(blank=True, default=None, max_length=100)),
                ('inventaire', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inventairemagasin.inventairemagasin')),
            ],
        ),
    ]
