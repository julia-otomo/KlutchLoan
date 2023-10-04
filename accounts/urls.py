from django.urls import path
from .views import AccountCreateView, AccountDetailsView

urlpatterns = [
    path("accounts/<str:cpf>/", AccountCreateView.as_view()),
    path("accounts/<str:account_number>/", AccountDetailsView.as_view()),
]
