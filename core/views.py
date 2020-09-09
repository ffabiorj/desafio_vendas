from django.http import Http404
from core.models import Transacao
from core.serializers import TransacaoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class TransacaoList(APIView):
    """
    Uma simples viewset para lista todas as transacões
    ou cria uma nova transação.
    """

    def get(self, request, format=None):
        queryset = Transacao.objects.all()
        serializer = TransacaoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TransacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"aceito": True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
