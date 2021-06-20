from django.db import models

from registrarventadeentrada.models.Sede import Sede


class Entrada():

    #Atributos
    
    fechaVenta = models.DateField
    horaVenta = models.IntegerField
    monto = models.IntegerField
    numero = models.IntegerField
    sede = Sede
    tarifa = models.IntegerField

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