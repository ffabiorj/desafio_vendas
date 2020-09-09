import pytest
from django.urls import reverse


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
