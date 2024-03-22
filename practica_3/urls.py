from django.contrib import admin
from django.urls import path, include
from practica_1.views import index, saludo, segunda, dia_hoy, muestra_nombre, probando_template, agregar_curso
urlpatterns = [
    path("", index),
    path('admin/', admin.site.urls),
    path("saludo/", saludo),
    path("segunda/", segunda),
    path("dia_hoy/", dia_hoy),
    path("mi_nombre/<nombre>", muestra_nombre),
    path("probando_template/", probando_template),
    path("agregar/", agregar_curso),
    path("app_coder/", include ("app_coder.urls")),
]
#Para no tener todas la urls de cada app en este archivo que se tornaria ilegible.
#Se crea un archivo url en cada app.