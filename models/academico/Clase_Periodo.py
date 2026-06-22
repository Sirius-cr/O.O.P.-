from models.enums.Estado_Periodo import EstadoPeriodo

class Periodo:
    def __init__(self, nombre_periodo: str, fecha_inicio: str, fecha_final: str):
        self.nombre_periodo = nombre_periodo
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self._estado_periodo = EstadoPeriodo.PLANIFICACION
        self.ofertas_academicas = []

    def agregar_oferta_academica(self, oferta):
        if oferta not in self.ofertas_academicas:
            self.ofertas_academicas.append(oferta)

    @property
    def estado_periodo(self):
        return self._estado_periodo.value

    def iniciar_periodo(self):
        if self._estado_periodo == EstadoPeriodo.PLANIFICACION:
            self._estado_periodo = EstadoPeriodo.EN_CURSO
            return "Periodo iniciado"
        return "No se puede iniciar"

    def finalizar_periodo(self):
        if self._estado_periodo == EstadoPeriodo.EN_CURSO:
            self._estado_periodo = EstadoPeriodo.FINALIZADO
            return "Periodo finalizado"
        return "No se puede finalizar"