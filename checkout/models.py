from django.db import models
from django.utils import timezone
from transaction.models import Transaction




class Checkout(models.Model):
    datePay = models.DateField(default=timezone.now)
    dateCheck = models.DateField(default=timezone.now, blank=True)
    whoPay = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    typePay = models.CharField(max_length=100, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.datePay}\t[=====]\t{self.whoPay}"

