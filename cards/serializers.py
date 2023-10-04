from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            "id",
            "card_number",
            "expiration_date",
            "cvv",
            "front_image",
            "back_image",
            "selfie_image",
        ]

    def create(self, validated_data: dict) -> Card:
        return Card.objects.create(**validated_data)

    def update(self, instance: Card, validated_data: dict) -> Card:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
