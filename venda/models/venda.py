from django.db import models
from core.models.base import Cliente, Produto, Endereco
# Create your models here.



class Item(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return '{}: {}'.format(self.quantidade, self.produto)

class Carrinho(models.Model):
    itens = models.ManyToManyField(Item)
    
    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'

    def __str__(self):
        return '{}'.format(self.itens)

class Venda(models.Model):
    frete = models.DecimalField(decimal_places=2, max_digits=10)
    pagamento = models.CharField(max_length=100)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return '{}: {}'.format(self.cliente, self.carrinho)