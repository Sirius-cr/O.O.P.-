from models.institucion.Clase_Universidad import Universidad 
from models.patrones_diseno.strategy.ReporteStrategy import Reporte

class Carrera:
    """
    Representa una carrera universitaria ofrecida por la institución.
    Administra su código identificador, cupos, inscripciones, la malla curricular y su coordinador.
    """
    def __init__(self, id_carrera : str, nombre_carrera : str, capacidad_estudiantil : int, estudiantes_inscritos : int = 0 ):
        """
        Inicializa una nueva instancia de la clase Carrera.

        Parámetros:
        - id_carrera (str): Identificador único de la carrera.
        - nombre_carrera (str): Nombre de la carrera.
        - capacidad_estudiantil (int): Capacidad máxima de estudiantes que admite.
        - estudiantes_inscritos (int, opcional): Número inicial de estudiantes inscritos. Por defecto 0.
        """
        self._id_carrera = id_carrera  # Atributo protegido para el identificador único
        self.nombre_carrera = nombre_carrera
        self.capacidad_estudiantil = capacidad_estudiantil
        self.estudiantes_inscritos = estudiantes_inscritos
        self.malla_curricular = None   # Malla curricular asociada
        self.coordinador = None        # Coordinador a cargo de la carrera

    def asociar_coordinador(self, coordinador):
        """
        Asocia un coordinador a la carrera, asegurando la consistencia bidireccional de la relación.

        Parámetros:
        - coordinador (Coordinador): El coordinador a asociar.
        """
        if self.coordinador != coordinador:
            self.coordinador = coordinador
            coordinador.asociar_carrera(self)

    def crear_malla_curricular(self, codigo_malla: str, area_conocimiento: str):
        """
        Crea e inicializa la malla curricular correspondiente a esta carrera.

        Parámetros:
        - codigo_malla (str): Código único de la malla.
        - area_conocimiento (str): Área de conocimiento de la carrera.

        Retorna:
        - MallaCurricular: El objeto de la malla curricular recién creado.
        """
        from models.academico.Clase_MallaCurricular import MallaCurricular
        self.malla_curricular = MallaCurricular(codigo_malla, area_conocimiento, carrera=self)
        return self.malla_curricular
    
    @property
    def id_carrera(self) -> str:
        """
        Propiedad de solo lectura para obtener el ID de la carrera.
        """
        return self._id_carrera
        
    def __crear_lista_estudiantes(self):
        """
        Método privado de simulación para inicializar el listado de estudiantes.
        """
        return f"la lista de estudiantes ha sido creada, la lista cuenta con {self.estudiantes_inscritos}" 

    def mostrar_datos_carrera(self, formato_documento):
        """
        Genera un reporte con la información básica y estadística de la carrera.

        Parámetros:
        - formato_documento (str): Formato del documento generado (ej. "JSON", "Consola").

        Retorna:
        - Reporte: Instancia del reporte con la información estructurada.
        """
        contenido = (
            f"Código Carrera: {self._id_carrera}\n"
            f"Carrera:        {self.nombre_carrera}\n"
            f"Capacidad Máx:  {self.capacidad_estudiantil}\n"
            f"Inscritos:      {self.estudiantes_inscritos}"
        )
        # Corregido: Retorna un objeto Reporte (Contexto) en lugar de ReporteConsola directamente
        return Reporte("Reporte de Carrera", formato_documento, f"Dirección de Carrera: {self.nombre_carrera}", contenido)




    
        