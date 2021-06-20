from django.db import models

class DetalleExposicion(models.Model):
    
    lugar_asignado = models.CharField(max_length=100)

    #MetodosDetalleExposicion
    def buscarDuracionExtraObra(self):
        None

    def conocerObra(self):
        None

    def conocerPared(self):
        None