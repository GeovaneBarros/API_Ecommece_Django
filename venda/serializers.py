from rest_framework import serializers
from venda.models import venda

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = venda.Carrinho
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = venda.Venda
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = venda.Item
        fields = '__all__'