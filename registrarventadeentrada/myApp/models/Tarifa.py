from django.db import models

from registrarventadeentrada.myApp.models import TipoEntrada
from registrarventadeentrada.myApp.models.TipoVisita import TipoVisita


class Tarifa():

    #Atributos de la clase Tarifa
    fechaFinVigencia = models.DateField()
    fechaInicioVigencia= models.DateField()
    monto = models.IntegerField()
    montoAdicionalGuia = models.IntegerField()
    tipoDeEntrada = TipoEntrada
    tipoVisita = TipoVisita

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
        entrada = self.tipoDeEntrada.getNombre()
        tipovisita = self.tipoVisita.getnombre()
        tarifa = (monto,entrada,tipovisita)
        return tarifa
    
    
