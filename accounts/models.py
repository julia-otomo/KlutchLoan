from django.db import models


class AccountType(models.TextChoices):
    CURRENT_ACCOUNT = "current account"
    SAVINGS_ACCOUNT = "savings account"


class Account(models.Model):
    bank_label = models.CharField(max_length=50)
    account_type_label = models.CharField(
        max_length=20, choices=AccountType.choices, default=AccountType.CURRENT_ACCOUNT
    )
    account_number = models.CharField(max_length=20)
    client = models.OneToOneField("clients.Client", on_delete=models.CASCADE)
