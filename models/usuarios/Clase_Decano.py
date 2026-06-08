from models.usuarios.Clase_UsuarioAdministrativo import UsuarioAdministrativo
from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico

class Decano(UsuarioAdministrativo, UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, idDecano):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self._idDecano = idDecano
        
    def gestionarFacultad(self):
        print("Accediendo a las herramientas de gestión de la facultad...")
        return True

    def verHorario(self):
        print("El decano no posee un horario de clases asignado.")
        return []