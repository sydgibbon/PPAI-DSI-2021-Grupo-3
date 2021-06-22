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
    if request.method == 'POST':
        form = TarifaForm(request.POST)
        if form.is_valid():
            prueba = form.cleaned_data['post']
    else:
        form = TarifaForm()
    return render(
        request=request,
        template_name='templates/tarifas/main.html',
        context={
            'form' : form,
            'tarifas' : getTarifas(),
            'prueba' : prueba
        }
    )