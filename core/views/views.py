from django.shortcuts import render
from rest_framework import viewsets, permissions
from core.models.base import Marca, Contato, Endereco, Cliente, Categoria, SubCategoria, Produto
from core import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class ContatoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Contato.objects.all()
    serializer_class = serializers.ContatoSerializer

class EnderecoViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Endereco.objects.all()
    serializer_class = serializers.EnderecoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Marca.objects.all()
    serializer_class = serializers.MarcaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoriaViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer

class SubCategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SubCategoria.objects.all()
    serializer_class = serializers.SubCategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer

class TokenList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = self.request.user
        return Response({"token": user.auth_token.key})