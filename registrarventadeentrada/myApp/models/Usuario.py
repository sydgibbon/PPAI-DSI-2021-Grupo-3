from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    caducidad = models.DateField()

    #MetodosUsuario
    def conocerEmpleado(self):
        None

    def obtenerEmpleado(self):
        None

