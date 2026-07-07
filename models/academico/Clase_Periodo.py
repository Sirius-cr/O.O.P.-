from datetime import datetime
from models.enums.Estado_Periodo import EstadoPeriodo


class Periodo:
    def __init__(self, nombre_periodo: str, fecha_inicio: str, fecha_final: str):
        self.nombre_periodo = nombre_periodo
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self._estado_periodo = EstadoPeriodo.PLANIFICACION

    # CONSULTAR ESTADO DEL PERÍODO
    @property
    def estado_periodo(self):
        "Retorna el estado actual del período."
        return self._estado_periodo.value

    # INICIAR PERÍODO
    def iniciar_periodo(self):
        "Cambia el estado de PLANIFICACIÓN a EN CURSO."
        if self._estado_periodo == EstadoPeriodo.PLANIFICACION:

            self._estado_periodo = EstadoPeriodo.EN_CURSO

            print(
                f"[{self.nombre_periodo}] "
                f"¡El período académico ha iniciado y ahora está EN CURSO!"
            )

        else:
            print(
                f"No se puede iniciar. "
                f"El período ya se encuentra en estado: "
                f"{self._estado_periodo.value}"
            )

    # FINALIZAR PERÍODO
    def finalizar_periodo(self):
        "Cambia el estado de EN CURSO a FINALIZADO."
        if self._estado_periodo == EstadoPeriodo.EN_CURSO:

            self._estado_periodo = EstadoPeriodo.FINALIZADO

            print(
                f"[{self.nombre_periodo}] "
                f"El período académico ha sido FINALIZADO oficialmente."
            )

        else:
            print(
                f"No se puede finalizar un período "
                f"que está en estado: {self._estado_periodo.value}"
            )

    # CONSULTA DE ESTADOS
    def esta_en_planificacion(self):
        "Verifica si el período está en planificación."
        return self._estado_periodo == EstadoPeriodo.PLANIFICACION

    def esta_activo(self):
        "Verifica si el período está en curso."
        return self._estado_periodo == EstadoPeriodo.EN_CURSO

    def esta_finalizado(self):
        "Verifica si el período ha finalizado."
        return self._estado_periodo == EstadoPeriodo.FINALIZADO
    
    # DURACIÓN DEL PERÍODO
    def calcular_duracion_dias(self):
        "Calcula la duración del período académico en días."

        inicio = datetime.strptime(
            self.fecha_inicio,
            "%Y-%m-%d"
        )

        fin = datetime.strptime(
            self.fecha_final,
            "%Y-%m-%d"
        )

        return (fin - inicio).days

    # RESUMEN DEL PERÍODO
    def obtener_resumen(self):
        "Genera un resumen básico del período."

        return {
            "nombre_periodo": self.nombre_periodo,
            "fecha_inicio": self.fecha_inicio,
            "fecha_final": self.fecha_final,
            "estado": self.estado_periodo,
        }