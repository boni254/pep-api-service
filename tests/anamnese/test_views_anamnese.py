from django.urls import reverse
from rest_framework import status


class TestAddAnamneseApi:
    def test_post_anamnese(self, api_client):
        data = {
            "id": 123456,
            "paciente_id": 123,
            "data_anamnese": "2023-09-01",
            "profissional_id": 456,
            "historico_clinico": "Paciente com histórico de hipertensão.",
            "queixas_principais": "Dor de cabeça constante.",
            "habitos_vida": "Não fuma, faz exercícios regulares.",
            "historico_familiar": "Pai com histórico de diabetes.",
            "alergias": "Nenhuma.",
        }

        url = reverse("add_anamnese")
        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_200_OK

    def test_post_anamnese_bad_request(self, api_client):
        data = {
            "id": 123456,
        }

        url = reverse("add_anamnese")
        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
