from django.db import models
from .Tarifa import Tarifa
from .Exposicion import Exposicion
from .Empleado import Empleado

class Sede(models.Model):

    "Atributos de la clase Sede"
    cantMaximaVisitantes = models.IntegerField()
    cantMaxPorGuia = models.IntegerField()
    nombre = models.CharField(max_length=100)
    empleado_creo = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE, null=True)
    exposicion = models.ForeignKey(Exposicion, on_delete=models.CASCADE, null = True)

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
        exposiciones_vigentes = Exposicion.esVigente()
        for exp in exposiciones_vigentes:
            duracion = exp.calcularDuracionObrasExpuestas()
        return duracion

    def obtenerTarifasVigentes(self):
        tarifas_vigentes = Tarifa.objects.get('poner condicion que permita extraer las tarifas vigentes de la bd')
        for t in tarifas_vigentes:
            tarifa = t.mostrarMontosVigentes()
        return tarifa


