from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria

class Materia:
    """
    Representa una materia o asignatura académica dentro de la institución.
    Contiene la configuración de aprobación (nota mínima, asistencia mínima) y gestiona sus secciones asociadas.
    """

    def __init__(self, id_materia, nombre_materia,
        nota_minima=EstadoDeAprobacionMateria.NOTA_MINIMA_APROBACION.value,
        asistencia_minima=EstadoDeAprobacionMateria.ASISTENCIA_MINIMA.value):
        """
        Inicializa una nueva instancia de la clase Materia.

        Parámetros:
        - id_materia (str/int): Identificador único de la materia.
        - nombre_materia (str): Nombre de la asignatura.
        - nota_minima (float, opcional): Nota mínima requerida para aprobar la materia.
        - asistencia_minima (float, opcional): Porcentaje mínimo de asistencia requerido.
        """
        self.id_materia = id_materia
        self.nombre_materia = nombre_materia
        self.nota_minima = nota_minima
        self.asistencia_minima = asistencia_minima
        self.secciones = []      # Lista de secciones académicas creadas para esta materia
        self.notas_materia = []   # Lista para registros de notas de la materia

    def crear_plan_estudio(self):
        """
        Crea o genera el plan de estudios conceptual de esta materia.

        Retorna:
        - str: Mensaje indicando que el plan se ha creado exitosamente.
        """
        return "¡Has creado un plan de estudios con éxito!"

    def crear_seccion(self, id_seccion, capacidad_estudiantil):
        """
        Crea e inscribe una nueva sección académica para esta materia.

        Parámetros:
        - id_seccion (str/int): Identificador de la nueva sección.
        - capacidad_estudiantil (int): Cantidad máxima de alumnos para la sección.

        Retorna:
        - Seccion: El objeto de la sección creada y registrada.
        """
        from models.academico.Clase_Seccion import Seccion
        nueva_seccion = Seccion(id_seccion, capacidad_estudiantil, materia=self)
        self.secciones.append(nueva_seccion)
        return nueva_seccion

    def obtener_Secciones(self):
        """
        Devuelve el listado de secciones asociadas a la materia.

        Retorna:
        - list/str: Lista de objetos Seccion si existen, o una cadena indicando que no hay secciones.
        """
        return self.secciones if self.secciones else "No existen secciones"

    def buscar_seccion(self, id_seccion):
        """
        Busca una sección específica de esta materia mediante su ID.

        Parámetros:
        - id_seccion (str/int): Identificador de la sección a buscar.

        Retorna:
        - Seccion: El objeto Seccion si se encuentra, de lo contrario None.
        """
        for sec in self.secciones:
            if sec.id_seccion == id_seccion:
                return sec
        return None

    def cantidad_secciones(self):
        """
        Obtiene la cantidad total de secciones registradas para esta materia.

        Retorna:
        - int: Número de secciones creadas.
        """
        return len(self.secciones)