
from django.contrib import admin
from .models import Categoria, Produto, Cor, Tamanho, VariacaoProduto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "criado_em")
    list_filter = ("categoria",)
    search_fields = ("nome",)


@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo_hexadecimal")
    search_fields = ("nome",)


@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


class VariacaoProdutoInline(admin.TabularInline):
    model = VariacaoProduto
    extra = 1


@admin.register(VariacaoProduto)
class VariacaoProdutoAdmin(admin.ModelAdmin):
    list_display = ("produto", "cor", "tamanho", "preco", "estoque")
    list_filter = ("cor", "tamanho")
    search_fields = ("produto__nome",)