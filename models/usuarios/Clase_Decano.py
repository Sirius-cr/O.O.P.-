from models.usuarios.Clase_UsuarioAdministrativo import UsuarioAdministrativo
from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico

class Decano(UsuarioAdministrativo, UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, id_decano):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self._id_decano = id_decano
        
    def gestionar_facultad(self):
        print("Accediendo a las herramientas de gestión de la facultad...")
        return True

    def ver_horario(self):
        print("El decano no posee un horario de clases asignado.")
        return []