

class ReservaVisita:
    cantidadAlumnos = None
    cantidadAlumnosConfirmada = None
    duracionEstimada = None
    fechaHoraCreacion = None
    fechaHoraReserva = None
    horaFinReal = None
    horaInicioReal = None
    numeroReserva = None

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