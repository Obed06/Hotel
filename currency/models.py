from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ExchangeRate(models.Model):
    from_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name='from_rates', default=None, null=True)
    to_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name='to_rates', default=None, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return f"{self.from_currency} to {self.to_currency}: {self.rate}"
