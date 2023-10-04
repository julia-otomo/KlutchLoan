from django.db import models


class ContractType(models.TextChoices):
    MANUAL = "manual"
    AUTOMATIC = "automatic"


class Solicitation(models.Model):
    installment_interest = models.IntegerField(null=True)
    installment_interest_value = models.FloatField(null=True)
    comission = models.FloatField(null=True)
    comission_value = models.FloatField(null=True)
    installment_value = models.FloatField(null=True)
    card_number = models.CharField(max_length=16, null=True)
    desired_value = models.FloatField(null=True)
    total_loan = models.FloatField(null=True)
    contract_type = models.CharField(
        max_length=10, choices=ContractType.choices, default=ContractType.AUTOMATIC
    )
    client = models.ForeignKey(
        "clients.Client",
        on_delete=models.CASCADE,
        related_name="solicitations",
        null=True,
    )
    installment = models.ForeignKey(
        "rateTables.Installment",
        on_delete=models.PROTECT,
        related_name="solicitations",
        null=True,
    )
    rate_table = models.ForeignKey(
        "rateTables.RateTable",
        on_delete=models.PROTECT,
        related_name="solicitations",
        null=True,
    )
