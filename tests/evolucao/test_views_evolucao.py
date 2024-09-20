from django.urls import reverse
from rest_framework import status


class TestAddEvolucaoApi:
    def test_post_evolucao(self, api_client):
        data = {
            "id": 123456,
            "paciente_id": 123,
            "data_evolucao": "2023-09-01",
            "profissional_id": 456,
            "descricao": "Paciente em recuperação.",
            "sinais_vitais": "120/80 mmHg, 70 bpm",
            "status_clinico": "Melhora",
            "observacoes": "Sem complicações.",
        }

        url = reverse("add_evolucao")
        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_200_OK

    def test_post_evolucao_bad_request(self, api_client):
        data = {
            "id": 123456,
        }

        url = reverse("add_evolucao")
        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
