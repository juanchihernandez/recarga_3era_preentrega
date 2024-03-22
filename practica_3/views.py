from datetime import datetime as dt

from django.http import HttpResponse

# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context 
from django.template import loader
from app_coder.models import Curso

def probando_template(request):

    # # Abrimos el archivo html
    # mi_html = open('./plantillas/templates1.html')

    # # Creamos el template haciendo uso de la clase Template
    # plantilla = Template(mi_html.read())

    # # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    # mi_html.close()

    # # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    # mi_contexto = Context(
    #     {
    #         "nombre": "Juanchi",
    #         "apellido": "Saragoza",
    #         "notas": [10, 5 , 8, 6, 2]
    #     }
    # )

    # # Terminamos de construír el template renderizándolo con su contexto
    # documento = plantilla.render(mi_contexto)

    diccionario = {
        "nombre": "Juanchi",
        "apellido": "Saragoza",
        "notas": [10, 5 , 8, 6, 2]
    }

    plantilla = loader.get_template("templates1.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)





def index(request):
    return HttpResponse("Este es el index")

def saludo(request):
    return HttpResponse("Hola gente, por acá les habla Juan<br>Hi world")

def segunda(request):
    var= "Esta es la creación de mi segunda vista"
    return HttpResponse(var)

def dia_hoy(request):
    var= "Hoy es:<br>"
    var += str(dt.now())
    return HttpResponse(var)

def muestra_nombre(request, nombre):

    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"

    return HttpResponse(documentoDeTexto)

def agregar_curso(request):
    curso = Curso(nombre="C++", camada=150)
    curso.save()

    return HttpResponse("Curso guardado")