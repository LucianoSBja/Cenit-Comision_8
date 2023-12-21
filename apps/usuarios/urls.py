from django.urls import path

from . import views
from apps.usuarios.views import EditaUsuario, ListarUsuarios, EditaPerfil, BorrarUsuario
app_name = 'usuarios'

urlpatterns = [
    
    path('registro/', views.Registro.as_view(), name = 'registro'),
    path('Usuario/<int:pk>/editar', EditaUsuario.as_view(), name = 'editausuario'),
    path('Usuario/<int:pk>/borrar', BorrarUsuario.as_view(), name = 'borrarusuario'),
    path('Perfil/<int:pk>/editar', EditaPerfil.as_view(), name = 'editaperfil'),
    path('listarusuarios/', ListarUsuarios.as_view(), name = 'listarusuarios'),


]