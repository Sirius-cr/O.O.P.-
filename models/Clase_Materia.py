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
    
class Seccion:
    #en capacidadEsudiantil hay una sobreescritura o ?? está usando un atributo de la clase <Carrera>
    def __init__(self, lista_horarios, capacidad_estudiantil, estudiantes_inscritos):
        self.lista_horarios = lista_horarios
        self.capacidad_estudiantil = capacidad_estudiantil
        self.estudiantes_inscritos = estudiantes_inscritos

    def importar_lista(self):
        return f"la lista a sido importada con exito!"
    
class Horario:
    #agregacion con seccion
    def __init__(self, turno, hora_inicio, hora_fin, modalidad):
        self.turno = turno
        self.hora_inicio =hora_inicio
        self.hora_fin=hora_fin
        self.__modalidad=modalidad

    
class Aula:
    def __init__(self, identificador_aula):
        self.identificador_aula=identificador_aula

class AulaVirtual:
    def __init__(self, identidicador_aula_virtual, url):
        self.identificador_aula_virtual=identidicador_aula_virtual
        self.url=url
        
#composicion con <<interfaz>> con la clase de Materia

    