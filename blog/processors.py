from apps.noticias.models import Categoria, Noticia

#CATEGORIAS
def ctx_dic_categoria(request):
    ctx_categoria = {}
    ctx_categoria['categorias'] = Categoria.objects.all
    return ctx_categoria

# ARCHIVOS
def ctx_dic_history(request):
	ctx_history = {}
	ctx_history['fechas'] = Noticia.objects.dates('creado', 'month', order='DESC').distinct()
	return ctx_history