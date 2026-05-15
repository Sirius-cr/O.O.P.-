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



class Tareas(InstrumentoEvaluacion):
    def __init__(self, porcentaje_nota, tipo_evaluacion, modalidad_presentacion):
        super().__init__(porcentaje_nota, tipo_evaluacion, modalidad_presentacion)

    #otra ves usamos un abstracto asi que a partir de aqui usare los mismos metodos vale?
    def _modificar_actividad(self):
        pass
    
    def _establecer_fecha_inicio(self):
        pass

    def _establecer_fecha_final(self):
        pass
    #hasta aqui
    def _agregar_descripcion(self):
        pass

class ActividadEnClase(InstrumentoEvaluacion):
    def __init__(self, porcentaje_nota, tipo_evaluacion, modalidad_presentacion):
        super().__init__(porcentaje_nota, tipo_evaluacion, modalidad_presentacion)

    def _modificar_actividad(self):
        pass
    
    def _establecer_fecha_inicio(self):
        pass

    def _establecer_fecha_final(self):
        pass

class Leccion(InstrumentoEvaluacion):
    def __init__(self, porcentaje_nota, tipo_evaluacion, modalidad_presentacion):
        super().__init__(porcentaje_nota, tipo_evaluacion, modalidad_presentacion)

    def _modificar_actividad(self):
        pass
    
    def _establecer_fecha_inicio(self):
        pass

    def _establecer_fecha_final(self):
        pass

class Nota:
    def __init__(self, fecha_registro, nota_obtenida, observaciones, lista_calificaciones):
        self.fecha_registro=fecha_registro
        self.nota_obtenida=nota_obtenida
        self.observaciones=observaciones
        self.lista_calificaciones=lista_calificaciones

