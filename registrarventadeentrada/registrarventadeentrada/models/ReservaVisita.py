from django.db import models

class ReservaVisita:
    cantidadAlumnos = models.IntegerField
    cantidadAlumnosConfirmada = models.IntegerField
    duracionEstimada = models.IntegerField
    fechaHoraCreacion = models.DateField
    fechaHoraReserva = models.DateField
    horaFinReal = models.IntegerField
    horaInicioReal = models.IntegerField
    numeroReserva = models.IntegerField

    def getCantidadAlumnos(self):
        return self.cantidadAlumnos
    def getCantidadAlumnosConfirmada(self):
        return self.cantidadAlumnosConfirmada
    def getDuracionEstimada(self):
        return self.duracionEstimada
    def getFechaHoraCreacion(self):
        return self.fechaHoraCreacion
    def getFechaHoraReserva(self):
        return self.fechaHoraReserva
    def getHoraFinReal(self):
        return self.getHoraFinReal
    def getHoraInicioReal(self):
        return self.horaInicioReal
    def getNumeroReserva(self):
        return self.numeroReserva

    def setCantidadAlumnos(self,cantidadAlumnos):
        self.cantidadAlumnos = cantidadAlumnos
    def setCantidadAlumnosConfirmada(self,cantidadAlumnosConfirmada):
        self.cantidadAlumnosConfirmada = cantidadAlumnosConfirmada
    def setDuracionEstimada(self,duracionEstimada):
        self.duracionEstimada = duracionEstimada
    def setFechaHoraCreacion(self,fechaHoraCreacion):
        self.fechaHoraCreacion = fechaHoraCreacion
    def setFechaHoraReserva(self,fechaHoraReserva):
        self.fechaHoraReserva = fechaHoraReserva
    def setHoraFinReal(self,horaFinReal):
        self.getHoraFinReal = horaFinReal
    def setHoraInicioReal(self,horaInicioReal):
        self.horaInicioReal = horaInicioReal
    def setNumeroReserva(self,numeroReserva):
        self.numeroReserva = numeroReserva

    def sonParaFechaYHoraYSede(self):
        None