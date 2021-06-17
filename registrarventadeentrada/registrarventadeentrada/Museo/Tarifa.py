
from registrarventadeentrada.Museo import TipoEntrada


class Tarifa():

    #Atributos de la clase Tarifa
    fechaFinVigencia = None
    fechaInicioVigencia= None
    monto = 0
    montoAdicionalGuia = 0
    tipoDeEntrada = None
    tipoVisita = None

    #Metodos
    def new():
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
    
    
