from datetime import datetime
from models.enums.Estado_Periodo import EstadoPeriodo


class Periodo:
    """
    Representa un período académico (ej. semestre, ciclo lectivo) dentro de la institución.
    Administra las fechas de inicio/fin, calcula la duración del ciclo y controla el flujo de estados
    (PLANIFICACIÓN -> EN CURSO -> FINALIZADO).
    """

    def __init__(self, nombre_periodo: str, fecha_inicio: str, fecha_final: str):
        """
        Inicializa una nueva instancia del período académico.

        Parámetros:
        - nombre_periodo (str): Nombre identificativo del período (ej. "2026-I").
        - fecha_inicio (str): Fecha de inicio del período en formato "YYYY-MM-DD".
        - fecha_final (str): Fecha de finalización del período en formato "YYYY-MM-DD".
        """
        self.nombre_periodo = nombre_periodo
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self._estado_periodo = EstadoPeriodo.PLANIFICACION  # Estado inicial predeterminado

    # CONSULTAR ESTADO DEL PERÍODO
    @property
    def estado_periodo(self):
        """
        Propiedad que retorna el estado actual del período como una cadena.

        Retorna:
        - str: Valor textual del estado actual.
        """
        return self._estado_periodo.value

    # INICIAR PERÍODO
    def iniciar_periodo(self):
        """
        Cambia el estado del período de PLANIFICACIÓN a EN CURSO.
        Valida que el período no haya sido iniciado o finalizado anteriormente.
        """
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
        """
        Cambia el estado del período de EN CURSO a FINALIZADO.
        Valida que el período se encuentre actualmente activo (EN CURSO) antes de cerrarlo.
        """
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
        """
        Verifica si el período está en estado de PLANIFICACIÓN.

        Retorna:
        - bool: True si está en planificación, False en caso contrario.
        """
        return self._estado_periodo == EstadoPeriodo.PLANIFICACION

    def esta_activo(self):
        """
        Verifica si el período está actualmente activo (EN CURSO).

        Retorna:
        - bool: True si está en curso, False en caso contrario.
        """
        return self._estado_periodo == EstadoPeriodo.EN_CURSO

    def esta_finalizado(self):
        """
        Verifica si el período ya ha FINALIZADO.

        Retorna:
        - bool: True si está finalizado, False en caso contrario.
        """
        return self._estado_periodo == EstadoPeriodo.FINALIZADO
    
    # DURACIÓN DEL PERÍODO
    def calcular_duracion_dias(self):
        """
        Calcula la duración en días del período académico basándose en las fechas de inicio y finalización.

        Retorna:
        - int: Diferencia de días entre la fecha de fin y la fecha de inicio.
        """
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
        """
        Genera un diccionario que resume los datos generales y el estado del período académico.

        Retorna:
        - dict: Resumen con nombre, fecha de inicio, fecha final y estado actual del período.
        """
        return {
            "nombre_periodo": self.nombre_periodo,
            "fecha_inicio": self.fecha_inicio,
            "fecha_final": self.fecha_final,
            "estado": self.estado_periodo,
        }