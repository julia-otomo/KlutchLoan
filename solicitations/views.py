from rest_framework.exceptions import ValidationError
from rest_framework import generics
from .models import Solicitation
from .serializers import SolicitationSerializer


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
