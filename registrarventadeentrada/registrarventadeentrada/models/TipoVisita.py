from django.db import models

class TipoVisita():

    #Atributos
    
    nombre = models.CharField()
    
    #Metodos 
    
    def getnombre(self):
        return self.nombre

    def setnombre(self,x):
        self.nombre = x