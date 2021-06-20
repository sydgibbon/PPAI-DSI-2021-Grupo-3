from django.db import models

class Empleado():
    nombre = models.CharField()
    apellido = models.CharField()
    codigo_validacion = models.CharField()
    cuit = models.IntegerField()
    dni = models.IntegerField()
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

    def obtenerSede(self):
        None
