from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def inicio(request):
    return render(request, "home.html")


def curso(request):
    return render(request, "curso.html")


def profesores(request):
    return render(request, "profesores.html")


def estudiantes(request):
    return render(request, "estudiantes.html")


def entregable(request):
    return render(request, "entregables.html")

def home(request):
    return render(request, "home.html")