from django.shortcuts import render
from rest_framework.views import set_rollback
from venda.serializers import CarrinhoSerializer, VendaSerializer, ItemSerializer
from rest_framework import viewsets, permissions
from venda.models.venda import Carrinho, Venda, Item


class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer