from django.urls import path

from app_coder import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("cursos", views.cursos, name="Curso"),
    path("profesores", views.profesores),
    path("estudiantes", views.estudiantes),
    path("curso-form/", views.curso_form, name="CursoForm"),
    path("curso-form-2/", views.curso_form_2, name="CursoForm2")
]
