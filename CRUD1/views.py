from django.shortcuts import render, redirect
from .models import Usuario
from .form import UsuarioForm
# Create your views here.


def index(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuarios/index.html", {"usuarios": usuarios})


def create(request):
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, "usuarios/create.html", {"formulario": formulario})


def details(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "usuarios/details.html", {"usuario": usuario})


def edit(request, id):
    usuario = Usuario.objects.get(id=id)
    formulario = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('index')
    return render(request, "usuarios/edit.html", {"formulario": formulario})


def delete(request, id):
    usuario = Usuario.objects.get(id=id)
    if usuario:
        usuario.delete()
    return redirect('index')
