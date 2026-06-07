from models.enums.Estado_Periodo import EstadoPeriodo

class Periodo:
    def __init__(self, nombrePeriodo, fechaInicio, fechaFinal):
        self.nombrePeriodo = nombrePeriodo
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal
        self._estadoPeriodo = EstadoPeriodo.PLANIFICACION

    @property
    def estado_periodo(self):
        return self._estadoPeriodo.value

    def iniciarPeriodo(self):
        if self._estadoPeriodo == EstadoPeriodo.PLANIFICACION:
            self._estadoPeriodo = EstadoPeriodo.EN_CURSO
            print(f"[{self.nombrePeriodo}] ¡El periodo académico ha iniciado y ahora está EN CURSO!")
        else:
            print(f"No se puede iniciar. El periodo ya se encuentra en estado: {self._estadoPeriodo.value}")

    def finalizarPeriodo(self):
        if self._estadoPeriodo == EstadoPeriodo.EN_CURSO:
            self._estadoPeriodo = EstadoPeriodo.FINALIZADO
            print(f"[{self.nombrePeriodo}] El periodo académico ha sido FINALIZADO oficialmente.")
        else:
            print(f"No se puede finalizar un periodo que está en estado: {self._estadoPeriodo.value}")