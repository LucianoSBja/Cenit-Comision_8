from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactoForm

class Vw_ContactoUsuario(FormView):
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto:sucess')

    def form_valid(self, form):
        # Procesar el formulario y enviar el correo electrónico
        nombre_apellido = form.cleaned_data['nombre_apellido']
        email = form.cleaned_data['email']
        mensaje = form.cleaned_data['mensaje']
        asunto = form.cleaned_data['asunto']

        # Configura el contenido del correo electrónico
        subject = 'Nuevo mensaje de contacto'
        message_body = f'Nombre: {nombre_apellido}\nEmail: {email}\nMensaje: {mensaje}'
        from_email = 'luisminicucci@gmail.com'  # Cambia esto con tu dirección de correo electrónico

        # Envía el correo electrónico
        send_mail(subject, message_body, from_email, [email])

        return super().form_valid(form)
    
class Vw_Success(TemplateView):
    template_name = 'contacto/contacto_success.html'
    success_url = reverse_lazy('home') 
