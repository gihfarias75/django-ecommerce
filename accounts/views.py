
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django import forms

from .models import Usuario


class FormularioCadastro(forms.ModelForm):
    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput
    )

    confirmar_senha = forms.CharField(
        label="Confirmar senha",
        widget=forms.PasswordInput
    )

    class Meta:
        model = Usuario
        fields = ["nome", "sobrenome", "email"]
        labels = {
            "nome": "Nome",
            "sobrenome": "Sobrenome",
            "email": "E-mail",
        }

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()

        if Usuario.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Já existe uma conta cadastrada com este e-mail."
            )

        return email

    def clean(self):
        dados = super().clean()
        senha = dados.get("senha")
        confirmar_senha = dados.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error(
                "confirmar_senha",
                "As senhas não coincidem."
            )

        elif senha:
            from django.contrib.auth.password_validation import validate_password

            usuario = Usuario(
                email=dados.get("email", ""),
                nome=dados.get("nome", ""),
                sobrenome=dados.get("sobrenome", ""),
            )

            try:
                validate_password(senha, user=usuario)
            except forms.ValidationError as erro:
                self.add_error("senha", erro)

        return dados


def cadastrar_cliente(request):
    if request.user.is_authenticated:
        return redirect("admin:index") if request.user.is_staff else redirect("inicio")

    if request.method == "POST":
        formulario = FormularioCadastro(request.POST)

        if formulario.is_valid():
            usuario = formulario.save(commit=False)
            usuario.set_password(formulario.cleaned_data["senha"])
            usuario.save()

            login(request, usuario)
            messages.success(request, "Sua conta foi criada com sucesso!")

            return redirect("inicio")
    else:
        formulario = FormularioCadastro()

    return render(
        request,
        "accounts/cadastro.html",
        {"formulario": formulario}
    )
