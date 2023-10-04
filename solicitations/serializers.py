from rest_framework import serializers
from .models import Solicitation
from clients.serializers import ClientSerializer
from rateTables.serializers import (
    RateTableSerializer,
    InstallmentCreateUpdateSerializer,
)


class SolicitationSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    rate_table = RateTableSerializer(read_only=True)
    installment = InstallmentCreateUpdateSerializer(read_only=True)

    class Meta:
        model = Solicitation
        fields = [
            "id",
            "installment_interest",
            "installment_interest_value",
            "comission",
            "comission_value",
            "installment_value",
            "card_number",
            "desired_value",
            "total_loan",
            "contract_type",
            "client",
            "installment",
            "rate_table",
        ]

    def create(self, validated_data: dict) -> Solicitation:
        return Solicitation.objects.create(**validated_data)

    def update(self, instance: Solicitation, validated_data: dict) -> Solicitation:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
