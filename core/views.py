from django.http import Http404
from core.models import Transacao
from core.serializers import TransacaoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TransacaoListe(APIView):
    """
    Lista todas as transacões ou cria uma nova transação.
    """

    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
