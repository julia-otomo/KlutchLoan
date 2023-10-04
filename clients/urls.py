from django.urls import path
from .views import ClientListCreateView, ClientDetailsView

urlpatterns = [
    path("clients/", ClientListCreateView.as_view()),
    path("clients/<str:cpf>/", ClientDetailsView.as_view()),
]
