from django import forms
from .models import Contacto

class ContactoForm(forms.Form):
    nombre_apellido = forms.CharField(label='Su Nombre y Apellido', max_length=100)
    email = forms.EmailField(label='Su Email')
    mensaje = forms.CharField(label='Su Mensaje', widget=forms.Textarea)
    asunto = forms.CharField(label='Asunto', max_length=100)
