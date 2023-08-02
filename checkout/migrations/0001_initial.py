# Generated by Django 4.2 on 2023-07-26 19:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePay', models.DateField(default=django.utils.timezone.now)),
                ('dateCheck', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('typePay', models.CharField(blank=True, max_length=100)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('whoPay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction')),
            ],
        ),
    ]
