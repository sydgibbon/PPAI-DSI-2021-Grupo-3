from django import template
import datetime

register = template.Library()

@register.simple_tag
def add(a, b):
    return a+b
    
@register.simple_tag
def list(a, b):
    lista = a[int(b)-1]
    return lista.monto

@register.simple_tag
def total(a, b, c):
    index = int(b) - 1
    lista = a[index]
    resultado = lista.monto * int(c)
    return resultado

@register.simple_tag
def total(a, b, c):
    index = int(b) - 1
    lista = a[index]
    resultado = lista.monto * int(c)
    return resultado

@register.simple_tag
def returnDia():
    dia = datetime.datetime.today()
    return dia

@register.simple_tag
def returnHora():
    ahora = datetime.datetime.today()
    return ahora