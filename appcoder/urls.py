from django.urls import path
from appcoder.views import *
from django.contrib.auth.views import LogoutView


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
        path('delete_estudiantes/<estudiante_id>', delete_estudiantes),
        path('login/', login_request),
        path('registro/', registro),
        path('logout/', LogoutView.as_view(template_name = 'inicio.html'), name = 'logout'),
       # path('logout/', LogoutView.as_view(template_name = 'inicio.html'), name="Logout" )
        path('perfil/', perfilview),
        path('perfil/editarperfil/', editarperfil),
        path('perfil/changepass/', changepass),
        
]