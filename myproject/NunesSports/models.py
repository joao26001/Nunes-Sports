from django.db import models
#Nome do produto
#Código do produto
#Descrição do produto
#Preço do produt

class Produto(models.Model):
    nomeProduto = models.CharField(max_length = 100, default="")
    codigoProduto = models.CharField(max_length = 10)
    descricaoProduto = models.TextField(max_length = 500, default="")
    precoProduto = models.DecimalField(max_digits = 10, decimal_places = 2)

    class Meta:
        verbose_name = 'Produto'
    
    def __str__(self):
        return self.nomeProduto    