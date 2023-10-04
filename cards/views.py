import imghdr
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Card
from .serializers import CardSerializer
from clients.models import Client
from django.shortcuts import get_object_or_404


class ClientCardListCreateView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = "cpf"

    def get_queryset(self):
        get_client_cpf = self.kwargs.get("cpf")
        queryset = super().get_queryset()
        client = get_object_or_404(Client, cpf=get_client_cpf)

        client_cards = queryset.filter(client=client)

        return client_cards

    def perform_create(self, serializer):
        get_client_cpf = self.kwargs.get("cpf")

        client = get_object_or_404(Client, cpf=get_client_cpf)

        front_image = self.request.data.get("front_image")
        back_image = self.request.data.get("back_image")
        selfie_image = self.request.data.get("selfie_image")

        allowed_image_mime_types = ["jpeg", "png", "gif"]

        if (
            not imghdr.what(front_image, h=None) in allowed_image_mime_types
            or not imghdr.what(back_image, h=None) in allowed_image_mime_types
            or not imghdr.what(selfie_image, h=None) in allowed_image_mime_types
        ):
            return Response(
                {"error": "Os arquivos não são imagens válidas."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save(client=client)

        return super().perform_create(serializer)


class CardDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = "card_number"
