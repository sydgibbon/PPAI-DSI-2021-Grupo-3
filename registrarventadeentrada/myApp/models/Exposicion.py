from django.db import models

class Exposicion(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_fin = models.DateField()
    fecha_fin_replanificada = models.DateField()
    fecha_inicio = models.DateField()
    fecha_inicio_replanificada = models.DateField()
    hora_apertura = models.DateField()
    hora_cierre = models.DateField()

    #MetodosClaseExposicion
    def calcularDuracionObrasExpuestas(self):
        None

    def esVigente(self):
        None

