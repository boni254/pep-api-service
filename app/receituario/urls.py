from django.urls import path

from .views import AddReceituarioApi

urlpatterns = [
    path("", AddReceituarioApi.as_view(), name="add_receituario"),
]
