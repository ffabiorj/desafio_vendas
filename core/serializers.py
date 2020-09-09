from rest_framework import serializers
from core.models import Transacao


class TransacaoSerializer(serializers.ModelSerializer):
    valor = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=False
    )

    class Meta:
        model = Transacao
        fields = ["estabelecimento", "cliente", "valor", "descricao"]
