from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
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
            'password1',
            'password2'
        ]
        
class UpdateUsuarioForm(UserChangeForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    imagen = forms.ImageField(label='Imagen', required=False)
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)
    is_staff = forms.BooleanField(
        label="Colaborador",
        required=False,
        help_text="checkbox",
    )

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username', 
            'imagen',
            'email',
            'is_staff',
            'password1',
            'password2'
        ]