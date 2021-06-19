from registrarventadeentrada.registrarventadeentrada.Museo import Sesion

class GestorVentaDeEntrada:
    empleadoLogueado = GestorVentaDeEntrada.buscarEmpleadoLogueado()
    entradas = None
    sesionActual = None
    tarifas = None


    #MetodosGestor
    def actVisitantesEnPantalla(self):
        None

    def buscarCapacidadSede(self):
        None

    def buscarEmpleadoLogueado(self):
        sesionActual = actual.getEmpleadoEnSesion()
        empleado = sesionActual.obtenerEmpleado()
        return empleado

    def buscarExposicionVigente(self):
        None

    def buscarReservasParaAsistir(self):
        None

    def buscarSede(self):
        None

    def buscarTarifasDeSede(self):
        None

    def buscarUltimoNroEntrada(self):
        None

    def calDuracVisitaCompleto(self):
        None

    def cantidadEntradasAEmitir(self):
        None

    def generarEntradas(self):
        None

    def imprimirEntradas(self):
        None

    def obtenerFechaHoraActual(self):
        None

    def opcionVtaEntradas(self):
        None

    def tomarTarifasSeleccionadas(self):
        None

    def finCU(self):
        None