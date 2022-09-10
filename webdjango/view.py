from django.http import HttpResponse
from django.template import loader
from appcoder.models import Curso
from appcoder.models import Estudiante


def home(self, name):
    return HttpResponse(f'Hola soy {name}')

def inicio(request):
    return HttpResponse(f'hola inicio')

def homePage(self):
    lista = [1,2,3,4,5,6,7,8,9]
    data = {'nombre': 'Derick', 'apellido': 'Carcamo', 'lista' : lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

def curso1(self):
    planilla = loader.get_template('cursos.html')
    documento = planilla.render()
    return HttpResponse(documento)
#
# la def cursos la importo de appcoder funcion curso, y funcion estudiante.
def cursos(self,):
    #planilla = loader.get_template('cursos.html')
    curso = Curso(nombre="UX/UI", camada="12345")
    curso.save()
    
    documento = f'Curso: {curso.nombre} camada: {curso.camada}' 
    return HttpResponse(documento)


def estudiante(self,):
    estudiante = Estudiante(nombre="cristian", apellido= "Nozralah", email= "cnoz2001@yahoo.com.ar")
    estudiante.save()
    documento= f' Estudiante: {estudiante.nombre} {estudiante.apellido} {estudiante.email}'
    return HttpResponse(documento)