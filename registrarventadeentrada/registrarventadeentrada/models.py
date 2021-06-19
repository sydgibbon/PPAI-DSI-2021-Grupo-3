from django.db import models

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class DetalleExposicion(models.Model):
    lugar_asignado = None

    #MetodosDetalleExposicion
    def buscarDuracionExtraObra(self):
        None

    def conocerObra(self):
        None

    def conocerPared(self):
        None

class Empleado():
    nombre = models.CharField()
    apellido = models.CharField()
    codigo_validacion = models.CharField()
    cuit = models.CharField()
    dni = models.CharField()
    domicilio = models.CharField()
    fecha_ingreso = models.DateField()
    fecha_nacimiento = models.DateField()
    mail = models.EmailField()
    sexo = models.CharField()

    #MetodosEmpleado
    def conocerCargo(self):
        None

    def conocerHorario(self):
        None

    def getGuiaDisponibleEnHorario(self):
        None

    def getNombre(self):
        return self.nombre

class Entrada():

    #Atributos
    
    fechaVenta = models.DateField()
    horaVenta = models.DateField()
    monto = models.FloatField()
    numero = models.IntegerField()
    sede = models.CharField()
    tarifa = models.CharField()

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

class Exposicion():
    nombre = ""
    fecha_fin = models.DateField()
    fecha_fin_replanificada = models.DateField()
    fecha_inicio = models.DateField()
    fecha_inicio_replanificada = models.DateField()
    hora_apertura = models.DateField()
    hora_cierre = models.DateField()

    #MetodosClaseExposicion
    def calcularDuracionObrasExpuestas(self):
        None

    def esVigente(self):
        None

