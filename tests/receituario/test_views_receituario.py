from django.urls import reverse
from rest_framework import status


class TestAddReceituarioApi:
    def test_post_receituario(self, api_client):
        data = {
            "id": 123456,
            "paciente_id": 123,
            "data_receituario": "2023-09-01",
            "profissional_id": 456,
            "medicamento": "Paracetamol",
            "dosagem": "500mg",
            "frequencia_administracao": "A cada 6 horas",
            "duracao_tratamento": "5 dias",
            "observacoes": "Tomar após as refeições.",
        }

        url = reverse("add_receituario")
        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_200_OK

    def test_post_receituario_bad_request(self, api_client):
        data = {
            "id": 123456,
        }

        url = reverse("add_receituario")
        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
