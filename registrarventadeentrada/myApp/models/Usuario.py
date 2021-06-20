from django.db import models
from .Empleado import Empleado

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    caducidad = models.DateField()

    #MetodosUsuario
    def conocerEmpleado(self):
        None

    def obtenerEmpleado(self):
        empleado = Empleado.objects.get(id=dni)

