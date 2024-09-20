from rest_framework import serializers


class EvolucaoSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    paciente_id = serializers.IntegerField(required=True)
    data_evolucao = serializers.DateTimeField(required=True)
    profissional_id = serializers.IntegerField(required=True)
    descricao = serializers.CharField(required=True)
    sinais_vitais = serializers.CharField(required=False, allow_blank=True)
    status_clinico = serializers.CharField(required=False, allow_blank=True)
    observacoes = serializers.CharField(required=False, allow_blank=True)
