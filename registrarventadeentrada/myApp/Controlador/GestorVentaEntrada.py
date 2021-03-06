from registrarventadeentrada.myApp.models.Sesion import Sesion

class GestorVentaDeEntrada:
    empleadoLogueado = GestorVentaDeEntrada.buscarEmpleadoLogueado()
    entradas = None
    sesionActual = None
    sedeActual = GestorVentaDeEntrada.buscarSede()
    tarifas = GestorVentaDeEntrada.buscarTarifasDeSede() #Esto hay que mostrarlo
    tarifas_seleccionadas = None
    exposiciones_vigentes = GestorVentaDeEntrada.buscarExposicionVigente()



    #MetodosGestor
    def actVisitantesEnPantalla(self):
        None

    def buscarCapacidadSede(self):
        None

    def buscarEmpleadoLogueado(self):
        empleado = Sesion.getEmpleadoEnSesion()
        return empleado

    def buscarExposicionVigente(self):
        self.sedeActual.calcularDuracionExposicionVigentes()

    def buscarReservasParaAsistir(self):
        None


    def buscarSede(self):
        sedeActual = self.empleadoLogueado.obtenerSede()
        return sedeActual

    def buscarTarifasDeSede(self):
        tarifas_vigentes = self.sedeActual.obtenerTarifasVigentes()
        return tarifas_vigentes

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
