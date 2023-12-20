from django.urls import path
from . import views
from apps.contacto.views import Vw_ContactoUsuario, Vw_Success

app_name = 'contacto'

urlpatterns = [
    path('Contacto/', Vw_ContactoUsuario.as_view(), name='contacto'),
    path('Contacto/Success', Vw_Success.as_view(), name='sucess'),
]