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
            name='InventaireCuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('produits', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produit.produit')),
            ],
        ),
        migrations.CreateModel(
            name='LigneInventaireCuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('inventaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventairecuisine.inventairecuisine')),
            ],
        ),
    ]
