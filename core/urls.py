from django.urls import path, include
from core.views.views import MarcaViewSet, EnderecoViewset, ContatoViewSet, UserViewSet, ClienteViewSet, CategoriaViewset, SubCategoriaViewSet, ProdutoViewSet, TokenList
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'contatos', ContatoViewSet)
router.register(r'enderecos', EnderecoViewset)
router.register(r'users', UserViewSet)
router.register(r'clientes',ClienteViewSet)
router.register(r'categorias', CategoriaViewset)
router.register(r'subcategorias', SubCategoriaViewSet)
router.register(r'produtos', ProdutoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenList.as_view()),
]
