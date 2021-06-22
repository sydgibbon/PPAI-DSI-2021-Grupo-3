from django.http import HttpResponse

# Utilities
from datetime import datetime
from django.shortcuts import redirect, render
from .forms import *
from .models import *



def getTarifas():
    tarifa = Tarifa.objects.all()
    return tarifa

def postCtdadEntradas(request):
    if request.method == 'POST':
        form = CtdadEntradasForm(request.POST) 
        print(form)

        return render(
        request=request,
        template_name='templates/tarifas/main.html',
        context={
            'form' : form,
            'idTarifa': 1
        }
    )

def seleccionarTarifa(request):
    print = request.POST.get('id')
    if request.method == 'POST':
        form = TarifaForm(request.POST)
        if form.is_valid():
            print = request.POST()
    else:
        form = TarifaForm()
    return render(
        request=request,
        template_name='tarifas/main.html',
        context={
            'form' : form,
            'tarifas' : getTarifas(),
            'prueba' : print
        }
    )


def postDetalleEntradas(request):
    id = request.POST.get('id')
    ctdadEntradas = request.POST.get('ctdadEntradas')
    if request.method == 'POST':
        form = TarifaForm(request.POST)
        if form.is_valid():
            print = request.POST()
    else:
        form = TarifaForm()
    return render(
        request=request,
        template_name='tarifas/main.html',
        context={
            'form' : form,
            'tarifas' : getTarifas(),
            'idPost' : id,
            'ctdadEntradas' : ctdadEntradas
        }
    )

def confirmarEntrada(request):
    numero = request.POST.get('numero')
    monto = request.POST.get('monto')
    fechaVenta = datetime.strptime(request.POST.get('fechaVenta'), '%Y-%m-%d %H:%M:%S.%f')
    horaVenta = datetime.strptime(request.POST.get('horaVenta'), '%Y-%m-%d %H:%M:%S.%f')
    entrada = Entrada(numero = numero, monto = monto, fechaVenta = fechaVenta, horaVenta = horaVenta)
    entrada.save()
    return render(
        request=request,
        template_name='tarifas/exito.html',
        context={
        }
    )