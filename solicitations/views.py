from rest_framework import generics
from .models import Solicitation
from .serializers import SolicitationSerializer


class SolicitationListCreateView(generics.ListCreateAPIView):
    queryset = Solicitation.objects.all()
    serializer_class = SolicitationSerializer


class SolicitationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitation.objects.all()
    serializer_class = SolicitationSerializer
