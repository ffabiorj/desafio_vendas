import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_retorna_status_201(client):
    url = reverse("transacao")
    data = {
        "estabelecimento": "45.283.163/0001-67",
        "cliente": "45.283.163/0001-67",
        "valor": 600.00,
        "descricao": "Almoço em restaurante chique pago via Shipay!",
    }
    response = client.post(url, data=data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_retorna_aceito_verdadeiro(client):
    url = reverse("transacao")
    data = {
        "estabelecimento": "45.283.163/0001-67",
        "cliente": "45.283.163/0001-67",
        "valor": 600.00,
        "descricao": "Almoço em restaurante chique pago via Shipay!",
    }
    response = client.post(url, data=data)
    assert response.data == {"aceito": True}


@pytest.mark.django_db
def test_retorna_status_code_400(client):
    url = reverse("transacao")
    data = {
        "estabelecimento": 1,
        "cliente": 1,
        "valor": 600.00,
        "descricao": "",
    }
    response = client.post(url, data=data)
    assert response.status_code == 400
