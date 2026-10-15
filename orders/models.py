from django.conf import settings
from django.db import models


class Pedido(models.Model):

    class Status(models.TextChoices):
        PENDENTE = "pendente", "Pendente"
        PAGO = "pago", "Pago"
        ENVIADO = "enviado", "Enviado"
        ENTREGUE = "entregue", "Entregue"
        CANCELADO = "cancelado", "Cancelado"

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="pedidos",
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDENTE,
    )

    def __str__(self):
        return f"Pedido #{self.pk}"

    @property
    def valor_total(self):
        return sum((item.subtotal for item in self.itens.all()), 0)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="itens",
    )
    variacao = models.ForeignKey(
        "products.VariacaoProduto",
        on_delete=models.PROTECT,
    )
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} unidade(s) - Pedido #{self.pedido_id}"

    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario
