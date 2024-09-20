from django.urls import path

from .views import AddAnamneseApi

urlpatterns = [
    path("", AddAnamneseApi.as_view(), name="add_anamnese"),
]
