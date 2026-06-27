from models.academico.Clase_Periodo import Periodo
from models.academico.Clase_MallaCurricular import MallaCurricular

class OfertaAcademica:
    def __init__(self, periodo: Periodo, malla_curricular: MallaCurricular, cupos_disponibles: int):
        self.periodo = periodo
        self.malla_curricular = malla_curricular
        self.cupos_disponibles = cupos_disponibles
        self.estado_oferta = True
        self.malla_curricular.agregar_oferta_academica(self)
        self.periodo.agregar_oferta_academica(self)

    def actualizar_cupos(self, nuevos_cupos: int):
        self.cupos_disponibles = nuevos_cupos

    def _cerrar_oferta(self):
        self.estado_oferta = False

    def _consultar_disponibilidad(self):
        return self.estado_oferta and self.cupos_disponibles > 0

    def obtener_resumen(self):
        return {
            "periodo": self.periodo.nombre_periodo,
            "malla": self.malla_curricular.codigo_malla,
            "cupos": self.cupos_disponibles,
            "estado": self.estado_oferta
        }