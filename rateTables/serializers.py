from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import RateTable, Installment


class InstallmentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installment
        fields = ["id", "installment_number", "installment_interest", "comission"]

        extra_kwargs = {
            "name": {
                "validators": [UniqueValidator(queryset=Installment.objects.all())]
            },
        }

    def create(self, validated_data: dict) -> Installment:
        return Installment.objects.create(**validated_data)

    def update(self, instance: Installment, validated_data: dict) -> Installment:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class InstallmentGetSerializer(serializers.ModelSerializer):
    installment_value = serializers.SerializerMethodField()
    full_value = serializers.SerializerMethodField()

    class Meta:
        model = Installment
        fields = [
            "id",
            "installment_number",
            "installment_interest",
            "comission",
            "installment_value",
            "full_value",
        ]

    def get_installment_value(self, obj):
        if self.context["request"].method == "GET":
            value_param = self.context["request"].query_params.get("value")

            if value_param:
                value_param = float(value_param)

                calc = (
                    value_param + (value_param * (obj.installment_interest / 100))
                ) / obj.installment_number

                return calc

    def get_full_value(self, obj):
        if self.context["request"].method == "GET":
            value_param = self.context["request"].query_params.get("value")

            if value_param:
                value_param = float(value_param)

                calc = value_param + (value_param * (obj.installment_interest / 100))

                return calc


class RateTableSerializer(serializers.ModelSerializer):
    installments = InstallmentGetSerializer(many=True, read_only=True)

    class Meta:
        model = RateTable
        fields = ["id", "name", "installments"]

        extra_kwargs = {
            "name": {"validators": [UniqueValidator(queryset=RateTable.objects.all())]},
        }

    def create(self, validated_data: dict) -> RateTable:
        return RateTable.objects.create(**validated_data)

    def update(self, instance: RateTable, validated_data: dict) -> RateTable:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
