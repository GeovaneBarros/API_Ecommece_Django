from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contato(models.Model):
    celular = models.CharField(max_length=16)
    telefone = models.CharField(max_length=16, null=True)
    email = models.EmailField(max_length=64)


    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
    
    def __str__(self):
        return self.celular

class Endereco(models.Model):
    rua = models.CharField(max_length=64)
    numero = models.CharField(max_length=8)
    bairro = models.CharField(max_length=32)
    cidade = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
    def __str__(self):
        return ("Rua: {} Número: {} Bairro: {}".format(self.rua,self.bairro,self.cidade))

class Cliente(models.Model):
    nome = models.CharField(max_length=32)
    sobrenome = models.CharField(max_length=32)
    cpf = models.CharField(max_length=14)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contato = models.OneToOneField(Contato, on_delete=models.CASCADE)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return (self.nome + " " + self.sobrenome)

class Categoria(models.Model):
    nome = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome

class SubCategoria(models.Model):
    nome = models.CharField(max_length=32)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sub-Categoria"
        verbose_name_plural = "Sub-Categorias"

    def __str__(self):
            return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=64)
    descricao = models.CharField(max_length=512)
    preco = models.DecimalField(max_digits=16, decimal_places=2)
    subCategoria =  models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
    def __str__(self):
        return self.nome