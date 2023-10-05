from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from .models import Solicitation
from .serializers import SolicitationSerializer
from clients.models import Client
from rateTables.models import RateTable, Installment


class SolicitationListCreateView(generics.ListCreateAPIView):
    queryset = Solicitation.objects.all()
    serializer_class = SolicitationSerializer

    def perform_create(self, serializer):
        desired_value = serializer.validated_data.get("desired_value")

        if desired_value:
            if desired_value < 300 or desired_value > 10000:
                raise ValidationError(
                    {"message": "o valor desejado deve estar entre 300 e 10.000"}
                )

        serializer.save()
        return super().perform_create(serializer)


class SolicitationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitation.objects.all()
    serializer_class = SolicitationSerializer

    def perform_update(self, serializer):
        desired_value = serializer.validated_data.get("desired_value")
        if desired_value:
            if desired_value < 300 or desired_value > 10000:
                raise ValidationError(
                    {"message": "o valor desejado deve estar entre 300 e 10.000"}
                )

        client_id = self.request.query_params.get("client")

        rate_table_id = self.request.query_params.get("rateTable")

        installment_id = self.request.query_params.get("installment")

        if client_id:
            client = get_object_or_404(Client, id=int(client_id))
            serializer.save(client=client)

        if rate_table_id:
            rate_table = get_object_or_404(RateTable, id=int(rate_table_id))
            serializer.save(rate_table=rate_table)

        if installment_id:
            installment = get_object_or_404(Installment, id=int(installment_id))
            serializer.save(installment=installment)

        serializer.save()
        return super().perform_update(serializer)
