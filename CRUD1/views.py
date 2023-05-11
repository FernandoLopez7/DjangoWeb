from django.shortcuts import render, redirect
from .models import Usuario, Cliente, Contrato
from .form import UsuarioForm, UserRegisterForm, UserLoginForm, ClienteForm, ContratoForm, DateFilterForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, authenticate, login


from django.contrib import messages


def can_edit_user(user):
    return user.has_perm('CRUD1.can_edit_user')

# Create your views here.

# CRUD y algunas cosas del login
def index(request):
    usuarios = Usuario.objects.all()
    campo = usuarios.model._meta.fields
    return render(request, "usuarios/index.html", {"usuarios": usuarios, "campo": campo, "user": request.user})


@login_required
def usercreate(request):
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, "usuarios/create.html", {"formulario": formulario})


def userdetails(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "usuarios/details.html", {"usuario": usuario})

# @permission_required('CRUD1.can_edit_user')
@user_passes_test(can_edit_user, login_url='index')
@login_required
def useredit(request, id):
    usuario = Usuario.objects.get(id=id)
    formulario = UsuarioForm(request.POST or None,
                             request.FILES or None, instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('index')
    return render(request, "usuarios/edit.html", {"formulario": formulario})


@login_required
def userdelete(request, id):
    usuario = Usuario.objects.get(id=id)
    if usuario:
        usuario.delete()
    return redirect('index')

# Login, logout and register
# Login and register


def login_or_register(request):
    login_form = UserLoginForm(request.POST or None)
    register_form = UserRegisterForm(request.POST or None)
    if request.method == 'POST':

        # Registrar usuario
        if 'register' in request.POST:
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                # Autenticar al usuario recién registrado
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('index')
        # Iniciar sesión
        elif 'login' in request.POST:
            form = UserLoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('index')
    context = {'login_form': login_form, 'register_form': register_form}
    return render(request, 'registration/login.html', context)


# Logout
def exit(request):
    logout(request)
    return redirect('index')

# Mini core


def indexclientes(request):
    clientes = Cliente.objects.all()
    campo = clientes.model._meta.fields
    return render(request, "clientes/index.html", {"clientes": clientes, "campo": campo})


def clientescreate(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, "clientes/create.html", {"formulario": formulario})


def indexcontratos(request):
    contratos = Contrato.objects.all()
    campo = contratos.model._meta.fields
    return render(request, "contratos/index.html", {"contratos": contratos, "campo": campo})


def contratoscreate(request):
    formulario = ContratoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, "contratos/create.html", {"formulario": formulario})


def report(request):
    form = DateFilterForm(request.GET)
    if not form.data:
        form.errors.clear()
        return render(request, 'MiniCore/filtrofechas.html', {'form': form})
    if not form.is_valid():
        return render(request, 'MiniCore/filtrofechas.html', {'form': form})

    fecha_inicio = form.cleaned_data['fecha_inicio']
    fecha_fin = form.cleaned_data['fecha_fin']

    contratos = Contrato.objects.all()
    results = []
    for contrato in contratos:
        # Filter by creation date
        rango = contrato.fecha_creacion >= fecha_inicio and contrato.fecha_creacion <= fecha_fin
        if not rango:
            continue
        client = contrato.cliente
        # Find the client in the results and update it
        client_found = False
        for result in results:
            if result['client'] == client:
                client_found = True
                result['contratos'] += 1
                result['total_price'] += contrato.precio
                break
        # If the client is not in the results, add it
        if not client_found:
            results.append({
                'client': client,
                'contratos': 1,
                'total_price': contrato.precio
            })
    # Sort the results by total price
    results.sort(key=lambda result: result['total_price'], reverse=True)
    return render(request, 'MiniCore/filtrofechas.html', {
        'form': form,
        'results': results,
        'summary': {
            'contratos': sum(result['contratos'] for result in results),
            'total_price': sum(result['total_price'] for result in results),
            'clients': len(results)
        }
    })