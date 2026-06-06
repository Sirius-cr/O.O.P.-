from models.Clases_InstrumentoEvaluacion import InstrumentoEvaluacion

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

    def calcular_puntaje(self):
        return self.porcentaje_nota * 1.0