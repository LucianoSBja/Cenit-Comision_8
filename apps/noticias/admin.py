from django.contrib import admin

from .models import Categoria, Noticia, Comentario

admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Comentario)

class NoticiasAdmin(Noticia):
    list_display = ('id', 'titulo', 'resumen', 'cuerpo', 'imagen', 'categoria_noticia', 'creado', 'modificado')
class ComentariosAdmin(Comentario):
    list_display = ('usuario', 'texto', 'noticia', 'fecha')
    
class CategotiasAdmin(Categoria):
    list_display = ('nombre')