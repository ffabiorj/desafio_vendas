import pytest
from django.urls import reverse
from core.models import Transacao


@pytest.mark.django_db
def test_retorna_status_200(client):
    url = reverse("transacao")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_retorna_vazio(client):
    url = reverse("transacao")
    response = client.get(url)
    assert response.data == []


@pytest.mark.django_db
def test_returna_um_pagamento(client):
    Transacao.objects.create(
        estabelecimento="45.283.163/0001-67",
        cliente="45.283.163/0001-67",
        valor=600.00,
        descricao="Almoço em restaurante chique pago via Shipay!",
    )
    url = reverse("transacao")
    response = client.get(url)
    data = data = [
        {
            "estabelecimento": "45.283.163/0001-67",
            "cliente": "45.283.163/0001-67",
            "valor": 600.00,
            "descricao": "Almoço em restaurante chique pago via Shipay!",
        }
    ]
    print(response.data)
    assert response.data == data
