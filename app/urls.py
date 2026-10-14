from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

from accounts.views import cadastrar_cliente


def inicio(request):
    return HttpResponse("Bem-vindo à loja!")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio, name="inicio"),
    path("cadastro/", cadastrar_cliente, name="cadastro"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )