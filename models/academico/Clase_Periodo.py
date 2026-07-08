from models.enums.Estado_Periodo import EstadoPeriodo

class Periodo:
    def __init__(self, nombre_periodo: str, fecha_inicio: str, fecha_final: str):
        self.nombre_periodo = nombre_periodo
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        # Usamos el Enum para un control estricto del estado inicial
        self._estado_periodo = EstadoPeriodo.PLANIFICACION
        self.ofertas_academicas = []

    def agregar_oferta_academica(self, oferta):
        if oferta not in self.ofertas_academicas:
            self.ofertas_academicas.append(oferta)

    @property
    def estado_periodo(self):
        """El decorador property permite leer el valor sin poder modificarlo directamente"""
        return self._estado_periodo.value

    def iniciar_periodo(self):
        if self._estado_periodo == EstadoPeriodo.PLANIFICACION:
            self._estado_periodo = EstadoPeriodo.EN_CURSO
            print(f"[{self.nombre_periodo}] ¡El periodo académico ha iniciado y ahora está EN CURSO!")
        else:
            print(f"No se puede iniciar. El periodo ya se encuentra en estado: {self._estado_periodo.value}")

    def finalizar_periodo(self):
        if self._estado_periodo in (EstadoPeriodo.EN_CURSO, EstadoPeriodo.PLANIFICACION):
            self._estado_periodo = EstadoPeriodo.FINALIZADO
            print(f"[{self.nombre_periodo}] El periodo académico ha sido FINALIZADO oficialmente.")
        else:
            print(f"No se puede finalizar un periodo que está en estado: {self._estado_periodo.value}")