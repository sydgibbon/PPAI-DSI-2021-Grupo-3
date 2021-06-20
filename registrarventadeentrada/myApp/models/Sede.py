from django.db import models

class Sede(models.Model):

    "Atributos de la clase Sede"
    cantMaximaVisitantes = models.IntegerField()
    cantMaxPorGuia = models.IntegerField()
    nombre = models.CharField(max_length=100)
    tarifa = models.IntegerField()

    "Metodos de la clase Sede"

    "Metodos get"
    def getCantMaximaVisitantes(self):
        return self.cantMaximaVisitantes
    def getCantMaxPorGuia(self):
        return self.cantMaxPorGuia
    def getNombre(self):
        return self.nombre

    "Metodos set"
    def setCantMaximaVisitantes(self,cantMaximaVisitantes):
        self.cantMaximaVisitantes = cantMaximaVisitantes
    def setCantMaxPorGuia(self,cantMaxPorGuia):
        self.cantMaxPorGuia = cantMaxPorGuia
    def setNombre(self,nombre):
        self.nombre = nombre

    def conocerExposicion(self):
        None

    def buscarDuracionExposicion(self):
        None

    def buscarExposicion(self):
        None

    def calcularDuracionExposicionVigentes(self):
        None

    def obtenerTarifasVigentes(self):
        #Hay que revisar cuales son las tarifas vigentes y poner una condicion
        tarifas_vigentes = []
        for t in self.tarifa:
            tarifas_vigentes.append(t.mostarMontosVigente())
        return tarifas_vigentes

