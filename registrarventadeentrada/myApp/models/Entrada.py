from django.db import models
from .Tarifa import Tarifa
from .Sede import Sede


class Entrada(models.Model):

    #Atributos
    
    fechaVenta = models.DateField()
    horaVenta = models.DateField()
    monto = models.IntegerField()
    numero = models.IntegerField()
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, null=True)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE, null=True)

    #Metodos

    def getfechaVenta(self):
        return self.fechaVenta 
    
    def gethoraVenta(self):
        return self.horaVenta

    def getmonto(self):
        return self.horaVenta
    
    def getnumero(self):
        return self.numero

    def getsede(self):
        return self.sede
    
    def gettarifa(self):
        return self.tarifa

    def setfechaVenta(self,x):
        self.fechaVenta = x

    def sethoraVenta(self,x):
        self.horaVenta = x

    def setmonto(self,x):
        self.monto = x
    
    def setnumero(self,x):
        self.numero = x

    def conocerGuiaAsignado(self):
        return