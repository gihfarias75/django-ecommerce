from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class GerenciadorUsuario(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **campos_adicionais):
        if not email:
            raise ValueError("O usuário precisa informar um e-mail.")

        email = self.normalize_email(email)
        usuario = self.model(email=email, **campos_adicionais)
        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, email, password=None, **campos_adicionais):
        campos_adicionais.setdefault("is_staff", True)
        campos_adicionais.setdefault("is_superuser", True)
        campos_adicionais.setdefault("is_active", True)

        if campos_adicionais.get("is_staff") is not True:
            raise ValueError("O superusuário precisa ter is_staff=True.")

        if campos_adicionais.get("is_superuser") is not True:
            raise ValueError("O superusuário precisa ter is_superuser=True.")

        return self.create_user(email, password, **campos_adicionais)


class Usuario(AbstractUser):
    username = None

    nome = models.CharField(
        max_length=150,
        verbose_name="Nome"
    )

    sobrenome = models.CharField(
        max_length=150,
        verbose_name="Sobrenome",
        blank=True
    )

    email = models.EmailField(
        unique=True,
        verbose_name="E-mail"
    )

    objects = GerenciadorUsuario()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
