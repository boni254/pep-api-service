from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="SuccessfulSerializer",
            description="Retorno com sucesso.",
            value={
                "status": "success",
                "message": "Dados recebidos com sucesso.",
            },
            response_only=True,
            status_codes=[200],
        ),
    ]
)
class SuccessfulSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="FieldsErrorSerializer",
            description="Retorno com erro na validação dos campos.",
            value={
                "paciente_id": ["Este campo é obrigatório."],
                "data_receituario": [
                    "Formato inválido para data e hora. Use um dos formatos a "
                    "seguir: YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]."
                ],
                "profissional_id": ["Este campo é obrigatório."],
            },
            response_only=True,
            status_codes=[200],
        ),
    ]
)
class FieldsErrorSerializer(serializers.Serializer):
    fields_name = serializers.ListField(child=serializers.CharField(label="message"))
