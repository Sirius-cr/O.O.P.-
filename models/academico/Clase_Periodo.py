from datetime import datetime
from models.enums.Estado_Periodo import EstadoPeriodo

class Periodo:
    def __init__(self, nombre_periodo, fecha_inicio, fecha_final):
        self.nombre_periodo = nombre_periodo
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self._estado_periodo = EstadoPeriodo.PLANIFICACION
        self.ofertas_academicas = []

    # AGREGAR OFERTA ACADÉMICA
    def agregar_oferta_academica(self, oferta):
        "Agrega una oferta académica al período evitando duplicados."
        if oferta not in self.ofertas_academicas:
            self.ofertas_academicas.append(oferta)

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

    # CAMBIAR ESTADO
    def cambiar_estado(self, nuevo_estado):
        "Permite cambiar el estado utilizando el Enum EstadoPeriodo."
        if isinstance(nuevo_estado, EstadoPeriodo):
            self._estado_periodo = nuevo_estado
            return (
                f"Estado actualizado correctamente a: "
                f"{nuevo_estado.value}"
            )
        return "Estado inválido."

    # OFERTAS ACADÉMICAS
    def tiene_ofertas(self):
        "Verifica si existen ofertas académicas registradas."
        return len(self.ofertas_academicas) > 0

    # CUPOS DISPONIBLES
    def cupos_totales(self):
        "Calcula la suma de cupos ofertados en el período."
        return sum(
            oferta.cupos_disponibles
            for oferta in self.ofertas_academicas
        )
    
    # LISTAR MALLAS OFERTADAS
    def listar_mallas(self):
        "Retorna los códigos de las mallas curriculares ofertadas."
        return [
            oferta.malla_curricular.codigo_malla
            for oferta in self.ofertas_academicas
        ]

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
            "cantidad_ofertas": len(self.ofertas_academicas),
            "cupos_totales": self.cupos_totales()
        }