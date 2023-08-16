# Generated by Django 4.2 on 2023-08-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix_vente', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
