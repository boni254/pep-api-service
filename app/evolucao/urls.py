from django.urls import path

from .views import AddEvolucaoApi

urlpatterns = [
    path("", AddEvolucaoApi.as_view(), name="add_evolucao"),
]
