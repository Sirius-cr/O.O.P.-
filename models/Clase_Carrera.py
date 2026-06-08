from models.Clase_Universidad import Universidad 
from models.Clase_Reporte import Reporte
#en tal caso de que se programe la composición lo dejaré de esta manera

class Carrera:
    def __init__(self, id_carrera, nombre_carrera, capacidad_estudiantil, estudiantes_inscritos):
        self._id_carrera = id_carrera #este tipo de atributo es protegido o ( # en uml)
        self.nombre_carrera = nombre_carrera
        self.capacidad_estudiantil = capacidad_estudiantil
        self.estudiantes_inscritos = estudiantes_inscritos
        
    def __crear_lista_estudiantes(self): #esta funcion es privada segun yo se pone asi
        return f"la lista de estudiantes a sido creada, la lista cuenta con {self.estudiantes_inscritos}" 

    def generarReporte(self, formatoDocumento):
        contenido = (
            f"Código Carrera: {self._id_carrera}\n"
            f"Carrera:        {self.nombre_carrera}\n"
            f"Capacidad Máx:  {self.capacidad_estudiantil}\n"
            f"Inscritos:      {self.estudiantes_inscritos}"
        )
        return Reporte("Reporte de Carrera", formatoDocumento, f"Dirección de Carrera: {self.nombre_carrera}", contenido)

    

    
        