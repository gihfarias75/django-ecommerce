from django.contrib import admin
from .models import Categoria, Produto, Cor, Tamanho, VariacaoProduto

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)
    
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao", "categoria", "criado_em")
    search_fields = ("nome", "descricao")
    list_filter = ("categoria",)
    
@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo_hexadecimal")
    search_fields = ("nome",)
    
@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    
@admin.register(VariacaoProduto)
class VariacaoProdutoAdmin(admin.ModelAdmin):
    list_display = ("produto", "cor", "tamanho", "preco", "estoque")
    search_fields = ("produto__nome", "cor__nome", "tamanho__nome")
    list_filter = ("produto", "cor", "tamanho")
    list_editable = ("preco", "estoque")