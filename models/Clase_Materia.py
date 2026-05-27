class Materia:
    def __init__(self, id_materia, nombre_materia, id_docente, lista_estudiantes, nombre_periodo, lista_instrumentos_evaluativos, nota_minima, asistencia_minima):
        self.id_materia = id_materia
        self.nombre_materia = nombre_materia
        self.id_docente = id_docente
        self.lista_estudiantes = lista_estudiantes
        self.nombre_periodo = nombre_periodo
        self.lista_instrumentos_evaluativos = lista_instrumentos_evaluativos
        self.nota_minima = nota_minima
        self.asistencia_minima = asistencia_minima

    def crear_plan_estudio(self):
        return f"Felciidades! has creado un plan de estudios con exito"

    def __importar_plan_estudio(self):
        return f"El plan de estudios a sido importado"
    
    def __subir_actividad(self):
        return f"{self.nombre_materia} ==> La actividad a sido subida"
    
    def __eliminar_actividad(self):
        return f"{self.nombre_materia} ==> La actvidad a sido borrada"
    
    def __modificar_actividad(self):
        return f"{self.nombre_materia} ==> La actividad a sido modificada"
    
    def __calcular_promedio(self):
        return f"el promedio es... CALCULADO XD"
    


    


    