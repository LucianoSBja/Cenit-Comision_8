from django.db import models
from apps.usuarios.models import Usuario
from django.utils import timezone

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)
 
	class Meta:
			ordering=('nombre',)

	def __str__(self):
		return self.nombre

class Noticia(models.Model):

	titulo = models.CharField(max_length = 150)
	resumen = models.CharField(max_length = 300, default=" ")
	cuerpo = models.TextField()
	imagen = models.ImageField(upload_to = 'noticias', default='static/noimagen.png')
	categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	creado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(default=timezone.now)
    
	class Meta:
			ordering=('-creado',)
 
	def __str__(self):
		return self.titulo

	def delete(self, using = None, keep_parents = False):
		self.imagen.delete(self.imagen.name)
		super().delete()
	
	def save(self, *args, **kwargs):
        # Actualizar la fecha de actualización antes de guardar
		self.modificado = timezone.now()
		super().save(*args, **kwargs)
  
class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	texto = models.TextField(max_length = 1500)
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f"{self.noticia}->{self.texto}"

	def delete(self, using = None, keep_parents = False):
		super().delete()
  
	def save(self, *args, **kwargs):
        # Actualizar la fecha de actualización antes de guardar
		self.modificado = timezone.now()
		super().save(*args, **kwargs)