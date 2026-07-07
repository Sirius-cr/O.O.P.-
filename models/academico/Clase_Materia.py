from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria

class Materia:
    def __init__(self, id_materia, nombre_materia,
        nota_minima=EstadoDeAprobacionMateria.NOTA_MINIMA_APROBACION.value,
        asistencia_minima=EstadoDeAprobacionMateria.ASISTENCIA_MINIMA.value):

        self.id_materia = id_materia
        self.nombre_materia = nombre_materia
        self.nota_minima = nota_minima
        self.asistencia_minima = asistencia_minima
        self.secciones = []
        self.notas_materia = []

    def crear_plan_estudio(self):
        return "¡Has creado un plan de estudios con éxito!"

    def crear_seccion(self, id_seccion, capacidad_estudiantil):
        from models.academico.Clase_Seccion import Seccion
        nueva_seccion = Seccion(id_seccion, capacidad_estudiantil, materia=self)
        self.secciones.append(nueva_seccion)
        return nueva_seccion

    def obtener_Secciones(self):
        return self.secciones if self.secciones else "No existen secciones"

    def buscar_seccion(self, id_seccion):
        for sec in self.secciones:
            if sec.id_seccion == id_seccion:
                return sec
        return None

    def cantidad_secciones(self):
        return len(self.secciones)    