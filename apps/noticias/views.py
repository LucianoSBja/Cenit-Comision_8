from datetime import timezone, datetime
from typing import Any
from django.shortcuts import render, redirect 
from django.core.cache import cache
from django.contrib.auth.decorators import login_required  #decorarod para VBF
from django.utils.decorators import method_decorator #decorador para VBC
#para trabajar con vistas basadas en clases
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .models import Noticia, Categoria, Comentario

from django.urls import reverse_lazy, reverse
from .forms import frm_Noticia, frm_Comentario

#  ************  VISTAS SIN REQUERIR LOGIN******************

#VISTA DE MI HOME. MUESTRA TODAS LAS NOTICIAS ORDENADAS POR MAS RECIENTES
class Vw_Muestra_Noticias(ListView):
	model = Noticia
	paginate_by = 5 #PAGINO CADA n NOTICIAS
	template_name = 'home.html'

#VISTA DE MI HOME. MUESTRA TODAS LAS NOTICIAS ORDENADAS POR CATEGORIA
class Vw_ordenoporcategoria(ListView):
	model = Noticia
	paginate_by = 5 #PAGINO CADA n NOTICIAS
	ordering=['categoria_noticia']
	template_name = 'home.html'
#VISTA DE MI HOME. MUESTRA TODAS LAS NOTICIAS ORDENADAS POR ORDEN ALFABETIDO DE TITULO ASC
class Vw_ordenoportitulo(ListView):
	model = Noticia
	paginate_by = 5 #PAGINO CADA n NOTICIAS
	ordering=['titulo']
	template_name = 'home.html'

#VISTA DE MI HOME. MUESTRA TODAS LAS NOTICIAS ORDENADAS POR ORDEN ALFABETIDO DE TITULO DES
class Vw_ordenoportitulo_des(ListView):
	model = Noticia
	paginate_by = 5 #PAGINO CADA n NOTICIAS
	ordering=['-titulo']
	template_name = 'home.html'
 
#VISTA DE MI HOME. MUESTRA TODAS LAS NOTICIAS ORDENADAS POR FECHA DE CREACION ASC
class Vw_ordenoporcreado(ListView):
	model = Noticia
	paginate_by = 5 #PAGINO CADA n NOTICIAS
	ordering=['creado']
	template_name = 'home.html' 
 
#MUESTRO UNA NOTICIA CON SUS COMENTARIOS
def Detalle_Noticias(request, pk):
	noti = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO
	cmt = Comentario.objects.filter(noticia = noti) #FILTRO COMENTARIOS DE ESE ID DE NOTICIA
	return render(request, 'noticias/detalle.html',{'noticia':noti, 'comentarios':cmt})
 
#MUESTRO NOTICIAS POR SU CATEGORIA
def porcategoria(request, pk):
	cate = Categoria.objects.get(pk=pk) #OBTENGO EL ID DE CATEGORIA QUE VIENE DE LA URL
	noti = Noticia.objects.filter(categoria_noticia=cate) #FILTRO LAS NOTICIAS QUE TENGAN ESA CATEGORIA
	return render(request, 'noticias/porcategoria.html',{'categoria':cate,'noticias':noti})


#  ************  VISTAS QUE REQUIEREN LOGIN******************

#VISTA PARA CREAR UNA NOTICIA
@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class Vw_Nueva_noticia(CreateView):
	model = Noticia
	Noticia.modificado = Noticia.creado
	fields = ['titulo', 'cuerpo', 'imagen', 'categoria_noticia']
	#form_class = frm_Nueva_Noticia
	template_name = 'noticias/nueva.html'
	success_url = reverse_lazy('home') 
 
#VISTA PARA COMENTAR UNA NOTICIA
@login_required #DECORADOR QUE CONTROLA LOGIN
def Comentar_Noticia(request):
    
	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	coment = Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)
 
	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))

@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class Vw_Borra_Comentario(DeleteView):
	model = Comentario	
	template_name = "noticias/confirmar_elimina_comentario.html"
	noti = Comentario.noticia.get_object
	success_url = reverse_lazy('home')

	def get_success_url(self):
      # Redirige a la vista de detalles de la publicación después de eliminar el comentario
		return reverse_lazy('noticias:detalle', kwargs={'pk': self.object.noticia.pk})

@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class Vw_Edita_Comentario(UpdateView):
	model = Comentario
	fields = ['texto']
	formclass = frm_Comentario
	template_name = "noticias/comentar.html"
	success_url = reverse_lazy('home')

	#modifico la funcion form_valid de la clase para poder cambiar la fecha de modificacion	
	def form_valid(self, form):
        # Actualizar la fecha de actualización antes de guardar el formulario
		self.object.modificado = datetime.now()
		return super().form_valid(form)
	
	def get_success_url(self):
      # Redirige a la vista de detalles de la publicación después de eliminar el comentario
		return reverse_lazy('noticias:detalle', kwargs={'pk': self.object.noticia.pk})

@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class Vw_Edita_Noticia(UpdateView):
	model = Noticia
	fields = ['titulo', 'cuerpo', 'imagen', 'categoria_noticia']
	formclass = frm_Noticia
	template_name = "noticias/editar_noticia.html"
	success_url = reverse_lazy('home')
	
	#modifico la funcion form_valid de la clase para poder cambiar la fecha de modificacion
	def form_valid(self, form): 
        # Actualizar la fecha de actualización antes de guardar el formulario
		self.object.modificado = datetime.now()
		return super().form_valid(form)

	def get_success_url(self):
      # Redirige a la vista de detalles de la publicación después de eliminar el comentario
		return reverse_lazy('noticias:detalle', kwargs={'pk':  self.object.pk})

@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class Vw_Borra_Noticia(DeleteView):
	model = Noticia	
	template_name = "noticias/confirmar_elimina_noticia.html"
	success_url = reverse_lazy('home')
 
@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class Vw_Muestra_Categorias(ListView):
	model = Categoria
	template_name = 'noticias/categorias.html'

@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class Vw_Borra_Categoria(DeleteView):
	model = Categoria
	template_name = "noticias/confirmar_elimina_categoria.html"
	success_url = reverse_lazy('noticias:categorias')
 
@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class Vw_Edita_Categoria(UpdateView):
	model = Categoria
	fields = ['nombre']
	template_name = "noticias/editar_categoria.html"
	success_url = reverse_lazy('noticias:categorias')
 
@method_decorator(login_required, name='dispatch') #decorador que controla login en Vistas basadas en Clases
class Vw_Nueva_Categoria(CreateView):
	model = Categoria
	fields = ['nombre']
	template_name = 'noticias/crear_categoria.html'
	success_url = reverse_lazy('noticias:categorias') 


#{'nombre':'name', 'apellido':'last name', 'edad':23}
#EN EL TEMPLATE SE RECIBE UNA VARIABLE SEPARADA POR CADA CLAVE VALOR
# nombre
# apellido
# edad

'''
ORM

CLASE.objects.get(pk = ____)
CLASE.objects.filter(campos = ____)
CLASE.objects.all() ---> SELECT * FROM CLASE

'''