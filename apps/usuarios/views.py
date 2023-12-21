from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required  #decorarod para VBF
from django.utils.decorators import method_decorator #decorador para VBC
from django.contrib import messages
from .models import Usuario
from .forms import RegistroForm
# Create your views here.

class Registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'usuarios/registro.html'

@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class ListarUsuarios(ListView):
	model = Usuario
	paginate_by = 20 #PAGINO CADA n NOTICIAS
	template_name = 'usuarios/listarusuarios.html'

@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases 
class EditaUsuario(UpdateView):
    model = Usuario
    template_name = 'usuarios/updateusuario.html'
    fields = ['first_name',
            'last_name',
            'email',
            'is_staff']
    success_url = reverse_lazy('usuarios:listarusuarios')
    
@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class BorrarUsuario(DeleteView):
	model = Usuario
	template_name = "usuarios/confirmar_elimina_usuario.html"
	success_url = reverse_lazy('usuarios:listarusuarios')

@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class EditaPerfil(UpdateView):
    model = Usuario
    template_name = 'usuarios/updateperfil.html'
    fields = ['first_name',
            'last_name',
            'imagen',
            'email']
    success_url = reverse_lazy('home')

class LoginUsuario(LoginView):
    template_name = 'usuarios/login.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Nombre de usuario o contraseña incorrectos.')
        return response

    def get_success_url(self):
        # Personaliza la URL de redirección después del inicio de sesión exitoso
        return '/'  # Cambia esto a la URL que desees 

#class LogoutUsuario(LogoutView):
 #   template_name = 'usuarios/logout.html'


  #  def get_success_url(self) -> str:
   #     return reverse('home')  