from django.urls import path
from .views import SolicitationListCreateView, SolicitationDetailsView

urlpatterns = [
    path("solicitations/", SolicitationListCreateView.as_view()),
    path("solicitation/<int:pk>/", SolicitationDetailsView.as_view()),
]
