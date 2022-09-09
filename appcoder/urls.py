from django.urls import path
from appcoder.views import *



urlpatterns = [
        path('', inicio),
        path('curso/', curso),
        path('entregables/', entregable),
        path("estudiantes/", estudiantes),
        path('profesores/', profesores),

]