from django.db import models
from .Empleado import Empleado

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    caducidad = models.DateField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)

    #MetodosUsuario
    def conocerEmpleado(self):
        None

    def obtenerEmpleado(self):
        empleado = Empleado.objects.get(id=dni)
        return Empleado
