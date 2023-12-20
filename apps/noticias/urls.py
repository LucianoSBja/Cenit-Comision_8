from django.urls import path

from . import views

from apps.noticias.views import Vw_Nueva_noticia, Vw_ordenoporcategoria, Vw_ordenoportitulo,  Vw_ordenoportitulo_des, Vw_ordenoporcreado, Vw_Borra_Comentario, Vw_Edita_Comentario,  Vw_Edita_Noticia, Vw_Borra_Noticia, Vw_Muestra_Categorias, Vw_Borra_Categoria, Vw_Edita_Categoria, Vw_Nueva_Categoria


app_name = 'noticias'

urlpatterns = [
	
	path('Detalle/<int:pk>', views.Detalle_Noticias, name = 'detalle'),
 	path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
  	path('Comentario/<int:pk>/Borrar', Vw_Borra_Comentario.as_view(), name = 'comentario_borrar'),
    path('Comentario/<int:pk>/Editar', Vw_Edita_Comentario.as_view(), name = 'comentario_editar'),
    path('Nueva_Noticia/', Vw_Nueva_noticia.as_view(), name = 'nueva'),
    path('Noticia/Borrar/<int:pk>', Vw_Borra_Noticia.as_view(), name = 'noticia_borrar'),
    path('Noticia/Editar/<int:pk>', Vw_Edita_Noticia.as_view(), name = 'noticia_editar'),
 	path('porcategoria/<int:pk>', views.porcategoria, name = 'porcategoria'),
    path('ordenoporcategoria', Vw_ordenoporcategoria.as_view(), name ="ordenoporcategoria"),
    path('ordenoportitulo', Vw_ordenoportitulo.as_view(), name ="ordenoportitulo"),
	path('ordenoportitulo_des', Vw_ordenoportitulo_des.as_view(), name ="ordenoportitulo_des"),
	path('ordenoporcreado', Vw_ordenoporcreado.as_view(), name ="ordenoporcreado"),
    path('categorias', Vw_Muestra_Categorias.as_view(), name ="categorias"),
    path('Categoria/Borrar/<int:pk>', Vw_Borra_Categoria.as_view(), name = 'categoria_borrar'),
    path('Categoria/Editar/<int:pk>', Vw_Edita_Categoria.as_view(), name = 'categoria_editar'),
 	path('Categoria/Crear', Vw_Nueva_Categoria.as_view(), name = 'categoria_crear'),
  
    
]