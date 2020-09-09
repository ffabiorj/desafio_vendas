from rest_framework import serializerss
from core.models import Transacao


class TransacaoSerializer(serializerss.ModelSerializer):
    class Meta:
        model = Transacao
        exclude = []