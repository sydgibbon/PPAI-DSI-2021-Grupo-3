from django.db import models

from .TipoEntrada import TipoEntrada
from .TipoVisita import TipoVisita


class Tarifa(models.Model):

    #Atributos de la clase Tarifa
    fechaFinVigencia = models.DateField()
    fechaInicioVigencia= models.DateField()
    monto = models.IntegerField()
    montoAdicionalGuia = models.IntegerField()


    #Metodos
    def new(self):
        return
    
    def getfechaFinVigencia(self):
        return self.fechaFinVigencia
    

    def getfechaIncioVigencia(self):
        return self.fechaInicioVigencia

    def getmonto(self):
        return self.monto
    
    def getmontoAdicionalGuia(self):
        return self.montoAdicionalGuia

    def getTipoEntrada(self):
        return self.tipoDeEntrada
    
    def getipoVisita(self):
        return self.tipoVisita

    def setfechaFinVigencia(self, x):
        self.fechaFinVigencia = x

    def fechaInicioVigencia(self,x):
        self.fechaInicioVigencia = x

    def setmonto(self,x):
        self.monto = x
        
    def setmontoAdicionalGuia(self,x): 
        self.montoAdicionalGuia = x

    def mostrarMontosVigentes(self):
        monto = self.getmonto()
        entrada = TipoEntrada.getnombre()
        tipovisita = TipoVisita.getnombre()
        tarifa = (monto,entrada,tipovisita)
        return tarifa
    
    
