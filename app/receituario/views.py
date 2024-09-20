from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.core.rabbitmq import publish_to_rabbitmq
from project.serializers import FieldsErrorSerializer, SuccessfulSerializer

from .serializers import ReceituarioSerializer


class AddReceituarioApi(APIView):
    @extend_schema(
        auth=None,
        operation_id="add-receituario:v1",
        summary="Recebe dados de uma receituario.",
        request=ReceituarioSerializer,
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
                            "data_receituario": [
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
                name="Exemplo",
                value={
                    "id": 123456,
                    "paciente_id": 123456,
                    "data_receituario": "2020-01-01",
                    "profissional_id": 123456,
                    "medicamento": "Exemplo de medicamento.",
                    "dosagem": "Exemplo de dosagem.",
                    "frequencia_administracao": "Exemplo de frequência de administração.",
                    "duracao_tratamento": "Exemplo de duranção do tratamento.",
                    "observacoes": "Exemplo de observações.",
                },
                request_only=True,
                status_codes=[200],
            ),
        ],
    )
    def post(self, request):
        serializer = ReceituarioSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data | {"_data_type": "receituario"}
        publish_to_rabbitmq(data)

        return Response(
            {"status": "success", "message": "Receituario recebido com sucesso."},
            status=status.HTTP_200_OK,
        )
