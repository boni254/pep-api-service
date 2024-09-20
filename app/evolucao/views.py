from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.core.rabbitmq import publish_to_rabbitmq
from project.serializers import FieldsErrorSerializer, SuccessfulSerializer

from .serializers import EvolucaoSerializer


class AddEvolucaoApi(APIView):
    HTTP_200_RESPONSE = {"status": "success", "message": "Evolução recebida com sucesso."}

    @extend_schema(
        operation_id="add-evolucao:v1",
        summary="Recebe dados de uma evolução.",
        request=EvolucaoSerializer,
        responses={
            200: OpenApiResponse(
                response=SuccessfulSerializer,
                description="Retorno com sucesso.",
                examples=[
                    OpenApiExample(
                        name="SuccessfulSerializer",
                        value={
                            "status": "success",
                            "message": "Dados recebidos com sucesso.",
                        },
                        response_only=True,
                        status_codes=[200],
                    ),
                ],
            ),
            400: OpenApiResponse(
                response=FieldsErrorSerializer,
                description="Informa quais campos obrigatórios estão faltando ou o formato dos "
                "dados são inválidos.",
                examples=[
                    OpenApiExample(
                        name="HTTP_400",
                        value={
                            "paciente_id": ["Este campo é obrigatório."],
                            "data_evolucao": [
                                "Formato inválido para data e hora. Use um dos formatos a "
                                "seguir: YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]."
                            ],
                            "profissional_id": ["Este campo é obrigatório."],
                        },
                        response_only=True,
                        status_codes=[400],
                    ),
                ],
            ),
        },
        examples=[
            OpenApiExample(
                name="Evolução Exemplo",
                value={
                    "id": 123456,
                    "paciente_id": 123456,
                    "data_evolucao": "2020-01-01",
                    "profissional_id": 123456,
                    "descricao": "Exemplo de descrição.",
                    "sinais_vitais": "Exemplo de sinais vitais.",
                    "status_clinico": "Exemplo de status clínico.",
                    "observacoes": "Exemplo de observações.",
                },
                request_only=True,
                status_codes=[200],
            ),
        ],
    )
    def post(self, request):
        serializer = EvolucaoSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data | {"_data_type": "evolucao"}
        publish_to_rabbitmq(data)

        return Response(
            self.HTTP_200_RESPONSE,
            status=status.HTTP_200_OK,
        )
