from rest_framework import serializers


class ReceituarioSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    paciente_id = serializers.IntegerField(required=True)
    data_receituario = serializers.DateTimeField(required=True)
    profissional_id = serializers.IntegerField(required=True)
    medicamento = serializers.CharField(required=True)
    dosagem = serializers.CharField(required=True)
    frequencia_administracao = serializers.CharField(required=True)
    duracao_tratamento = serializers.CharField(required=True)
    observacoes = serializers.CharField(required=False, allow_blank=True)
