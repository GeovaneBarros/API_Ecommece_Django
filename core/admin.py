from django.contrib import admin
from .models import base
# Register your models here.
admin.site.register(base.Contato)
admin.site.register(base.Endereco)
admin.site.register(base.Cliente)
admin.site.register(base.Categoria)
admin.site.register(base.SubCategoria)
admin.site.register(base.Produto)
admin.site.register(base.Marca)