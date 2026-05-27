from abc import ABC, abstractmethod

class InstrumentoEvaluacion(ABC):
    def __init__(self, porcentaje_nota, tipo_evaluacion, modalidad_presentacion):
        self.porcentaje_nota=porcentaje_nota
        self.tipo_evaluacion=tipo_evaluacion
        self.modalidad_presentacion=modalidad_presentacion

    @abstractmethod
    def _modificar_actividad(self):
        pass
    
    @abstractmethod
    def _establecer_fecha_inicio(self):
        pass

    @abstractmethod
    def _establecer_fecha_final(self):
        pass
