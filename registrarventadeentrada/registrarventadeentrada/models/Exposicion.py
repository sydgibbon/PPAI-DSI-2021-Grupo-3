from django.db import models

class Exposicion():
    nombre = models.CharField
    fecha_fin = models.DateField
    fecha_fin_replanificada = models.DateField
    fecha_inicio = models.DateField
    fecha_inicio_replanificada = models.DateField
    hora_apertura = models.IntegerField
    hora_cierre = models.IntegerField

    #MetodosClaseExposicion
    def calcularDuracionObrasExpuestas(self):
        None

    def esVigente(self):
        None

