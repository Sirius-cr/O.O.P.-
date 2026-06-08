from Clase_UsuarioAcademico import UsuarioAcademico
from Clases_InstrumentoEvaluacion import GestorActividades

class Docente(UsuarioAcademico):
    def colocar_calificacion(self):
        print("Calificando actividad...")

# El Docente solo implementa la interfaz que realmente utiliza
class Docente_actividades(GestorActividades):
    def anadir_actividad(self):
        print("Actividad añadida a la sección")