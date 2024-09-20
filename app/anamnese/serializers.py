from rest_framework import serializers


class AnamneseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    paciente_id = serializers.IntegerField(required=True)
    data_anamnese = serializers.DateTimeField(required=True)
    profissional_id = serializers.IntegerField(required=True)
    historico_clinico = serializers.CharField(required=True)
    queixas_principais = serializers.CharField(required=True)
    habitos_vida = serializers.CharField(required=False, allow_blank=True)
    historico_familiar = serializers.CharField(required=False, allow_blank=True)
    alergias = serializers.CharField(required=False, allow_blank=True)
