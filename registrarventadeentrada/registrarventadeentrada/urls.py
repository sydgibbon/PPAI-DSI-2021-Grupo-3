"""registrarventadeentrada URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from registrarventadeentrada import views as local_views
from myApp import views as app_views
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', local_views.index),
    url(r'^$', local_views.index, name='tarifas'),
    url(r'^ctdadEntradas$', app_views.seleccionarTarifa),
    url(r'^detalleEntradas$', app_views.postDetalleEntradas),
    url(r'^confirmado$', app_views.confirmarEntrada)
]
