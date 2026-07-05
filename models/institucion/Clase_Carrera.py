from models.institucion.Clase_Universidad import Universidad 
from models.patrones_diseno.strategy.ReporteStrategy import Reporte
#en tal caso de que se programe la composición lo dejaré de esta manera

class Carrera:
    def __init__(self, id_carrera : str, nombre_carrera : str, capacidad_estudiantil : int, estudiantes_inscritos : int = 0 ):
        self._id_carrera = id_carrera #este tipo de atributo es protegido o ( # en uml)
        self.nombre_carrera = nombre_carrera
        self.capacidad_estudiantil = capacidad_estudiantil
        self.estudiantes_inscritos = estudiantes_inscritos
        self.malla_curricular = None
        self.coordinador = None

    def asociar_coordinador(self, coordinador):
        if self.coordinador != coordinador:
            self.coordinador = coordinador
            coordinador.asociar_carrera(self)

    def crear_malla_curricular(self, codigo_malla: str, area_conocimiento: str):
        from models.academico.Clase_MallaCurricular import MallaCurricular
        self.malla_curricular = MallaCurricular(codigo_malla, area_conocimiento, carrera=self)
        return self.malla_curricular
    
    @property
    def id_carrera(self) -> str:
        return self._id_carrera #Usar el property para que pueda ser accesible en las otras clases
        
    def __crear_lista_estudiantes(self): #esta funcion es privada segun yo se pone asi
        return f"la lista de estudiantes a sido creada, la lista cuenta con {self.estudiantes_inscritos}" 


    def mostrar_datos_carrera(self, formato_documento):
        contenido = (
            f"Código Carrera: {self._id_carrera}\n"
            f"Carrera:        {self.nombre_carrera}\n"
            f"Capacidad Máx:  {self.capacidad_estudiantil}\n"
            f"Inscritos:      {self.estudiantes_inscritos}"
        )
        return Reporte("Reporte de Carrera", formato_documento, f"Dirección de Carrera: {self.nombre_carrera}", contenido)



    
        