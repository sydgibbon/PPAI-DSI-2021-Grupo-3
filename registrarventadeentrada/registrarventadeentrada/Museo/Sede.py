class Sede:

    "Atributos de la clase Sede"
    cantMaximaVisitantes = 0
    cantMaxPorGuia = 0
    nombre = ""

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