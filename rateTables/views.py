from rest_framework import generics
from .models import RateTable, Installment
from .serializers import (
    InstallmentCreateUpdateSerializer,
    InstallmentGetSerializer,
    RateTableSerializer,
)
from django.shortcuts import get_object_or_404


class RateTableListCreateView(generics.ListCreateAPIView):
    queryset = RateTable.objects.all()
    serializer_class = RateTableSerializer


class RateTableDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RateTable.objects.all()
    serializer_class = RateTableSerializer


class InstallmentCreateView(generics.CreateAPIView):
    queryset = Installment.objects.all()
    serializer_class = InstallmentCreateUpdateSerializer

    def perform_create(self, serializer):
        table_pk = self.kwargs.get("pk")

        table = get_object_or_404(RateTable, pk=int(table_pk))

        serializer.save(rate_table=table)

        return super().perform_create(serializer)


class InstallmentRetrieveView(generics.RetrieveAPIView):
    queryset = Installment.objects.all()
    serializer_class = InstallmentGetSerializer


class InstallmentUpdateView(generics.UpdateAPIView):
    queryset = Installment.objects.all()
    serializer_class = InstallmentCreateUpdateSerializer


class InstallmentDeleteView(generics.DestroyAPIView):
    queryset = Installment.objects.all()
    serializer_class = InstallmentCreateUpdateSerializer
