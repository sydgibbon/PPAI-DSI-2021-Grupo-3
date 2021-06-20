from django.db import models

class Usuario():
    nombre = models.CharField()
    password = models.CharField()
    caducidad = models.DateField()

    #MetodosUsuario
    def conocerEmpleado(self):
        None

    def obtenerEmpleado(self):
        None

