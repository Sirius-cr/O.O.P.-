from abc import ABC, abstractmethod

class InstrumentoEvaluacion(ABC):
    def __init__(self, porcentaje_nota, tipo_evaluacion, modalidad_presentacion):
        self.porcentaje_nota = porcentaje_nota
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

    @abstractmethod
    def calcular_puntaje(self):
        pass
    
class GestorActividades(ABC):
    @abstractmethod
    def anadir_actividad(self):
        pass

class CalculadoraDeNotas:
    def calcular(self, instrumento: InstrumentoEvaluacion):
        # Cumple OCP: Llama a la abstracción sin importar qué clase hija sea.
        return instrumento.calcular_puntaje()
