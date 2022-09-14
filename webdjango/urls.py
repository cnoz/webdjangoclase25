"""webdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from webdjango.view import home, homePage, cursos
from webdjango.view import estudiante, curso1, inicio, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio),
    path('home/<name>', home),
    path('homePage/', homePage),
    path('cursos/', cursos),
    path('estudiante/',estudiante),
    path('curso1/',curso1),
    path('appcoder/', include("appcoder.urls")),
    
]
