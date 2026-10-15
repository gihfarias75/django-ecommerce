
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="produtos",
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Cor(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    codigo_hexadecimal = models.CharField(max_length=7, blank=True)

    def __str__(self):
        return self.nome


class Tamanho(models.Model):
    nome = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nome


class VariacaoProduto(models.Model):
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name="variacoes",
    )
    cor = models.ForeignKey(
        Cor,
        on_delete=models.PROTECT,
    )
    tamanho = models.ForeignKey(
        Tamanho,
        on_delete=models.PROTECT,
    )
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["produto", "cor", "tamanho"],
                name="variacao_produto_cor_tamanho_unica",
            )
        ]

    def __str__(self):
        return f"{self.produto} - {self.cor} - {self.tamanho}"
