from django.db import models

class TipoEntrada(models.Model):

    #Atributos
    
    nombre = models.CharField(max_length=100)
    
    #Metodos 
    
    def getnombre(self):
        return self.nombre

    def setnombre(self,x):
        self.nombre = x