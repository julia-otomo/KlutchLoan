from django.db import models
from cloudinary.models import CloudinaryField


class Card(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    expiration_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=4)
    front_image = CloudinaryField("image")
    back_image = CloudinaryField("image")
    selfie_image = CloudinaryField("image")
    client = models.ForeignKey(
        "clients.Client", on_delete=models.CASCADE, related_name="cards"
    )
