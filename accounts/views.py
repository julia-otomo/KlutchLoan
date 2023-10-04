from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer
from clients.models import Client
from django.shortcuts import get_object_or_404


class AccountCreateView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = "cpf"

    def perform_create(self, serializer):
        get_client_cpf = self.kwargs.get("cpf")

        client = get_object_or_404(Client, cpf=get_client_cpf)

        serializer.save(client=client)

        return super().perform_create(serializer)


class AccountDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = "account_number"
