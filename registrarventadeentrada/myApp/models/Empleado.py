from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    codigo_validacion = models.CharField(max_length=100)
    cuit = models.IntegerField()
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    fecha_nacimiento = models.DateField()
    mail = models.EmailField()
    sexo = models.CharField(max_length=100)

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
