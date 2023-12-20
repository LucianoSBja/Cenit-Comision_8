from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    #tipo_usuario = forms.CharField(label='Tipo', required=True)
    imagen = forms.ImageField(label='Imagen', required=False)
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username', 
            'imagen',
            'email',
         #   'tipo',
            'password1',
            'password2'
        ]