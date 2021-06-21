from django.db import models
from .Obra import Obra

class DetalleExposicion(models.Model):
    
    lugar_asignado = models.CharField(max_length=100)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, null=True)


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
