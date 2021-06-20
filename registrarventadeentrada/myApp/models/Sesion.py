from django.db import models

class Sesion(models.Model):
    fecha_fin = models.DateField()
    fecha_inicio = models.DateField()
    hora_fin = models.DateField()
    hora_inicio = models.DateField()

    #MetodosSesion
    def conocerUsuario(self):
        None

    def getEmpleadoEnSesion(self):
        None