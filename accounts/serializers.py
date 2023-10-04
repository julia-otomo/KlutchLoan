from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "bank_label", "account_type_label", "account_number"]

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
