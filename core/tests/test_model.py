import pytest
from core.models import Transacao


@pytest.mark.django_db
def test_criar_transacao():
    Transacao.objects.create(
        estabelecimento="45.283.163/0001-67",
        cliente="45.283.163/0001-67",
        valor=600.00,
        descricao="Almoço em restaurante chique pago via Shipay!",
    )
    assert Transacao.objects.count() == 1


@pytest.mark.django_db
def test_str_de_transacao():
    resultado = Transacao.objects.create(
        estabelecimento="45.283.163/0001-67",
        cliente="45.283.163/0001-67",
        valor=600.00,
        descricao="Almoço em restaurante chique pago via Shipay!",
    )
    assert resultado.__str__() == "Almoço em restaurante chique pago via Shipay!"
