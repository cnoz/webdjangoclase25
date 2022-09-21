from django.urls import path
from appcoder.views import *



urlpatterns = [
        path('', inicio),
        path('curso/', curso),
        path('entregables/', entregable),
        path("estudiantes/", estudiantes),
        path('profesores/', profesores),
        path('home/', home),
        path("api_estudiantes/", api_estudiantes),
        path("buscar_estudiante/", buscar_estudiante),

        path('create_estudiantes/', create_estudiantes),
        path('read_estudiantes/', read_estudiantes),
        path('update_estudiantes/<estudiante_id>', update_estudiantes),
        path('delete_estudiantes/<estudiante_id>', delete_estudiantes)
]