from rest_framework import serializers
from .models import Client
from rest_framework.validators import UniqueValidator
from accounts.serializers import AccountSerializer
from cards.serializers import CardSerializer


class ClientSerializer(serializers.ModelSerializer):
    bank = AccountSerializer(read_only=True)
    cards = CardSerializer(read_only=True, many=True)

    class Meta:
        model = Client
        fields = ["id", "name", "cpf", "phone", "bank", "cards"]

        extra_kwargs = {
            "cpf": {"validators": [UniqueValidator(queryset=Client.objects.all())]},
            "phone": {"validators": [UniqueValidator(queryset=Client.objects.all())]},
        }

    def create(self, validated_data: dict) -> Client:
        return Client.objects.create(**validated_data)

    def update(self, instance: Client, validated_data: dict) -> Client:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
