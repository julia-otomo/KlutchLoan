from django.db import models


class RateTable(models.Model):
    name: models.CharField(max_length=25, unique=True)


class Installment(models.Model):
    installment_number = models.IntegerField()
    installment_interest = models.IntegerField()
    rate_table = models.ForeignKey(
        RateTable, on_delete=models.CASCADE, related_name="installments"
    )
