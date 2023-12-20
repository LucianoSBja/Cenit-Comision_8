from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.noticias.models import Noticia, Categoria

#request 'es un diccionario que continuamente se va pasando entre el navegador y el servidor'

def Home(request):

	return render(request, 'home.html')


def Nosotros(request):

	return render(request, 'nosotros.html')


def test(request):
    
    return render(request, 'test.html')

"""class Vw_HomePageView(TemplateView):
    template_name = "home.html"
       
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        n = Noticia.objects.all() #RETORNA UNA LISTA DE OBJETOS
        ctx['noticias'] = n
        cat = Categoria.objects.all().order_by('nombre')
        ctx['categorias'] = cat
        return ctx
"""