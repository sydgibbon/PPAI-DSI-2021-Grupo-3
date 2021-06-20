from django.db import models
from .Usuario import Usuario

class Sesion(models.Model):
    fecha_fin = models.DateField()
    fecha_inicio = models.DateField()
    hora_fin = models.DateField()
    hora_inicio = models.DateField()

    #MetodosSesion
    def conocerUsuario(self):
        None

    def getEmpleadoEnSesion(self):
        empleado = Usuario.obtenerEmpleado()
        return empleado