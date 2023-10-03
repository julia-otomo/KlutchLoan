from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=25)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=12, unique=True)
