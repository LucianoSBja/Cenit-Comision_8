from django import forms
from .models import Categoria, Comentario, Noticia

class frm_Nueva_Noticia(forms.Form):
    titulo = forms.CharField(label="Titulo de la noticia", max_length=150)
    cuerpo = forms.CharField(label="Cuerpo", widget=forms.Textarea)
    imagen_noti = forms.ImageField(label="imagen", required=True)
    categoria_id = forms.ModelChoiceField(label="Categoria", queryset=Categoria.objects.all())
 
class frm_Comentario(forms.Form):
    class Meta:
        model = Comentario
        fields = ['texto', 'modificado']

class frm_Noticia(forms.Form):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'imagen_noti', 'categoria_id', 'modificado']


