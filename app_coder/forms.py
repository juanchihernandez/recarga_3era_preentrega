from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    # email = forms.EmailField()