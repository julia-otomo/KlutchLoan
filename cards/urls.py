from django.urls import path
from .views import ClientCardListCreateView, CardDetailsView

urlpatterns = [
    path("cards/client/<str:cpf>/", ClientCardListCreateView.as_view()),
    path("cards/<str:card_number>/", CardDetailsView.as_view()),
]
