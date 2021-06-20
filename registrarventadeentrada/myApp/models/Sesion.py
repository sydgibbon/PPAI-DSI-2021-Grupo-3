from django.db import models

class Sesion():
    fecha_fin = models.DateField
    fecha_inicio = models.DateField
    hora_fin = models.SmallIntegerField
    hora_inicio = models.SmallIntegerField

    #MetodosSesion
    def conocerUsuario(self):
        None

    def getEmpleadoEnSesion(self):
        None