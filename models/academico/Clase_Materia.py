from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria

class Materia:
    def __init__(self, id_materia, nombre_materia, nota_minima = EstadoDeAprobacionMateria.NOTA_MINIMA_APROBACION.value, asistencia_minima = EstadoDeAprobacionMateria.ASISTENCIA_MINIMA.value):
        
        self.id_materia = id_materia
        self.nombre_materia = nombre_materia
        self.nota_minima = nota_minima
        self.asistencia_minima = asistencia_minima
        self.secciones = []
        self.notas_materia = []  # Relación 0..* con NotaMateria

    def crear_plan_estudio(self):
        return f"Felciidades! has creado un plan de estudios con exito"

    def crear_seccion(self, id_seccion, capacidad_estudiantil):
        from models.academico.Clase_Seccion import Seccion
        nueva_seccion = Seccion(id_seccion, capacidad_estudiantil, materia=self)
        self.secciones.append(nueva_seccion)
        return nueva_seccion

    def obtener_Secciones(self):
        if len(self.secciones) == 0:
            return "No existe secciones creadas"
        return self.secciones

    


    


    