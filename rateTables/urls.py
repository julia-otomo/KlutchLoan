from django.urls import path
from .views import (
    RateTableListCreateView,
    RateTableDetailsView,
    InstallmentCreateView,
    InstallmentRetrieveView,
    InstallmentUpdateView,
    InstallmentDeleteView,
)

urlpatterns = [
    path("rateTable/", RateTableListCreateView.as_view()),
    path("rateTable/<int:pk>/", RateTableDetailsView.as_view()),
    path("installment/table/<int:pk>/", InstallmentCreateView.as_view()),
    path("installment/retrieve/<int:pk>/", InstallmentRetrieveView.as_view()),
    path("installment/update/<int:pk>/", InstallmentUpdateView.as_view()),
    path("installment/delete/<int:pk>/", InstallmentDeleteView.as_view()),
]
