from django.contrib import admin
from venda.models.venda import Carrinho, Venda, Item
# Register your models here.
admin.site.register(Carrinho)
admin.site.register(Venda)
admin.site.register(Item)