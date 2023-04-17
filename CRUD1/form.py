# Esto era para el form de las tablas usuario del propio Django
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Esto era para el form de las tablas creadas
from django.forms import ModelForm
from .models import Usuario, Cliente, Contrato

# CRUD


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

# Login, logout and register


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # contraseña1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    # contraseña2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # help_texts = {k:"" for k in fields }


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

# Mini core


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ContratoForm(ModelForm):
    # cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), label='Cliente')
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        label='Cliente',
        to_field_name='nombre',  # aquí especificamos el campo 'nombre' en lugar del campo 'id'
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    class Meta:
        model = Contrato
        fields = ['cliente', 'descripcion', 'precio']
        widgets = {
            'cliente': forms.Select(),
            # 'fecha_edicion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class DateFilterForm(forms.Form):
    fecha_inicio = forms.DateField(
        label='Fecha de inicio',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    fecha_fin = forms.DateField(
        label='Fecha de fin',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    def __init__(self, *args, **kwargs):
        super(DateFilterForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(DateFilterForm, self).clean()
        fecha_inico = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        if fecha_inico and fecha_fin:
            if fecha_inico > fecha_fin:
                raise forms.ValidationError(
                    'La fecha de inicio no debe ser mayor que la fecha de fin')
        return cleaned_data
