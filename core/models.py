from django.db import models


class Transacao(models.Model):
    estabelecimento = models.CharField(max_length=30, blank=False, null=False)
    cliente = models.CharField(max_length=30, blank=False, null=False)
    valor = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    descricao = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.descricao