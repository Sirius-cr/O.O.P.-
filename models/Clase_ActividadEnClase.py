from models.Clases_InstrumentoEvaluacion import InstrumentoEvaluacion

class ActividadEnClase(InstrumentoEvaluacion):
    def __init__(self, porcentaje_nota, tipo_evaluacion, modalidad_presentacion):
        super().__init__(porcentaje_nota, tipo_evaluacion, modalidad_presentacion)

    def _modificar_actividad(self):
        pass
    
    def _establecer_fecha_inicio(self):
        pass

    def _establecer_fecha_final(self):
        pass