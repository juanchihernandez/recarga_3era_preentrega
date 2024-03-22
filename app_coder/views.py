from django.shortcuts import render
from django.http import HttpResponse
from app_coder.models import Curso, Profesor, Estudiante
from app_coder.forms import CursoFormulario


# Create your views here.

def inicio(request):
    return render(request, "padre.html")
    #return HttpResponse("vista inicio")

def cursos(request):

    return render(request, "cursos.html", {"cursos":cursos})
    #return HttpResponse("vista cursos")

def profesores(request):
    return render(request, "padre.html")

def estudiantes(request):
    return render(request, "padre.html")

def curso_form(request):

    if request.method == 'POST':
        
        curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
        
        curso.save()
        
        return render(request, "padre.html")

    return render(request, "curso_formulario.html")

def curso_form_2(request):

    if request.method == "POST":

        miFormulario = CursoFormulario(request.POST)
        print(f"\n\n\n{{miFormulario}}")

        if miFormulario.is_valid():
        
            informacion = miFormulario.cleaned_data

            curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso.save()
        return render(request, "padre.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "cursoFormulario.html", {"miFormulario": miFormulario})