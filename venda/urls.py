from django.urls import path, include
from rest_framework import routers
from venda.views.views import CarrinhoViewSet, VendaViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'vendas', VendaViewSet)
router.register(r'carrinhos', CarrinhoViewSet)
router.register(r'itens', ItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
