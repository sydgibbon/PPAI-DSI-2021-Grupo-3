from django.http import HttpResponse

# Utilities
from datetime import datetime
from django.shortcuts import redirect, render
from .models import *

def getTarifas():
    tarifa = Tarifa.objects.all()
    return tarifa

def postCtdadEntradas(request):
    if request.method == 'POST':
        ctdadEntradas = request.POST['ctdadEntradas']
    return redirect(true)
