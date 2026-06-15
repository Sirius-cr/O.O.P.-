# Importaciones exactas simulando tu estructura de carpetas
from models.academico.Clase_Periodo import Periodo
from models.academico.Clase_MallaCurricular import MallaCurricular

class OfertaAcademica:
    def __init__(self, periodo: Periodo, malla_curricular: MallaCurricular, cupos_disponibles: int):
        # Guardamos los objetos completos en memoria
        self.periodo = periodo
        self.malla_curricular = malla_curricular
        self.cupos_disponibles = cupos_disponibles
        self.estado_oferta = True

        # Registrar automáticamente las referencias bidireccionales
        self.malla_curricular.agregar_oferta_academica(self)
        self.periodo.agregar_oferta_academica(self)

    def actualizar_cupos(self, nuevos_cupos: int) -> None:
        """Actualiza el valor de los cupos. No retorna nada."""
        self.cupos_disponibles = nuevos_cupos

    def _cerrar_oferta(self) -> None:
        """Método protegido. Cambia el estado a inactivo. No retorna nada."""
        self.estado_oferta = False

    def _consultar_disponibilidad(self) -> bool:
        """Evalúa si hay cupos y si la oferta está activa."""
        return self.estado_oferta and self.cupos_disponibles > 0