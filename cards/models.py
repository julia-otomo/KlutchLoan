from django.db import models


class Card(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    expiration_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=4)
    front_image = models.ImageField()
    back_image = models.ImageField()
    selfie_image = models.ImageField()
    client = models.ForeignKey(
        "clients.Client", on_delete=models.CASCADE, related_name="cards"
    )
