from django.urls import path
from core import views

urlpatterns = [path("transacao/", views.TransacaoList.as_view(), name="transacao")]
