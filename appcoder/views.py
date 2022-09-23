from django.shortcuts import render, redirect
from django.http import HttpResponse
from appcoder.models import Estudiante
from appcoder.forms import form_estudiantes, UserRegisterForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inicio(request):
    return render(request, "home.html")



def curso(request):
    return render(request, "curso.html")

def profesores(request):
    return render(request, "profesores.html")

def estudiantes(request):
    if request.method == "POST":
        estudiante = Estudiante(nombre=request.POST['nombre'], apellido=request.POST['apellido'],email=request.POST['email'])
        estudiante.save()
        return render(request, "home.html")
    return render(request, "estudiantes.html")

def entregable(request):
    return render(request, "entregables.html")

def home(request):
    return render(request, "home.html")

def api_estudiantes(request):
    if request.method == "POST":
        formulario = form_estudiantes(request.POST)
        if formulario.is_valid(): 
            informacion = formulario.cleaned_data
            estudiante = Estudiante(nombre = informacion['nombre'], apellido = informacion['apellido'], email= informacion['email'])
            estudiante.save()
            return render(request, 'api_estudiantes.html')
    else:
        formulario = form_estudiantes()
    return render(request, 'api_estudiantes.html', {'formulario': formulario})

def buscar_estudiante(request):
    if request.GET['email']:
        email = request.GET['email']
        estudiantes = Estudiante.objects.filter(email__icontains= email)
        return render(request, "estudiantes.html", {'estudiantes': estudiantes})
    else:
        respuesta = "No enviaste datos"
    #return render(request, "estudiantes.html") #si no cargo datos se queda en la pag.
    return HttpResponse(respuesta)



def create_estudiantes(request):
    if request.method == 'POST':
        estudiante= Estudiante(nombre= request.POST['nombre'], apellido= request.POST['apellido'], email=request.POST['email'])
        estudiante.save()
        estudiantes = Estudiante.objects.all() #Trae todo
        return render(request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})
    return render(request,'estudiantesCRUD/create_estudiantes.html')


def read_estudiantes(request=None):
    estudiantes = Estudiante.objects.all() #Trae todo
    return render(request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})


def update_estudiantes(request, estudiante_id):
    estudiante = Estudiante.objects.get(id = estudiante_id)

    if request.method == 'POST':
        formulario = form_estudiantes(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante.nombre = informacion['nombre']
            estudiante.apellido = informacion['apellido']
            estudiante.email = informacion['email']
            estudiante.save()
            estudiantes = Estudiante.objects.all() #Trae todo
            return render(request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})
    else:
        formulario = form_estudiantes(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido, 'email': estudiante.email})
    return render(request,"estudiantesCRUD/update_estudiantes.html", {"formulario": formulario})



def delete_estudiantes(request, estudiante_id):
    estudiante= Estudiante.objects.get(id = estudiante_id)
    estudiante.delete()

    estudiantes = Estudiante.objects.all() #Trae todo
    return render(request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})
##################################
# 22/09/2022

def login_request(request):    
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)    
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user , password = pwd)

            if user is not None:
                login(request, user )
                return  render(request, 'home.html')
            
            else:
                return render(request, 'login.html', {'form': form })

        else:
            return render(request, 'login.html', {'form': form})

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form2 = UserRegisterForm(request.POST)
        print(form2)
        if form2.is_valid():
            #username = form.cleaned_data["username"]
            form2.save()
            #redirect("/appcoder/login/")
            #return render(request, "inicio.html")
            return redirect("/appcoder/login/")

    #form = UserCreationForm()
    form2 = UserRegisterForm()
    return render(request, "registro.html", {'form1': form2})

        