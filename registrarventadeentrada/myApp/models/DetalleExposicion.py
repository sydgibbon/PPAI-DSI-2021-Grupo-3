from django.db import models
from .Obra import Obra

class DetalleExposicion(models.Model):
    
    lugar_asignado = models.CharField(max_length=100)

    #MetodosDetalleExposicion
    def buscarDuracionExtraObra(self):
        None

    def conocerObra(self):
        None

    def conocerPared(self):
        None

    def buscarDuracionObra(self):
        duracion = Obra.getDuracionResumida()
        return duracion