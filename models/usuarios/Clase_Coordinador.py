from models.usuarios.Clase_UsuarioAdministrativo import UsuarioAdministrativo
from models.academico.Clase_Periodo import Periodo
from models.gestion.Clase_Reporte import GestorReportes

class Coordinador(UsuarioAdministrativo):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, id_coordinador, fecha_asignacion_cargo):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.id_coordinador = id_coordinador
        self.fecha_asignacion_cargo = fecha_asignacion_cargo
        
    def abrir_periodo_matricula(self, periodo: Periodo):
        periodo.iniciar_periodo()
        return True

    def cerrar_periodo_matricula(self, periodo: Periodo):
        periodo.finalizar_periodo()
        return True

    def aprobar_retiro(self):
        #Se implementará una vez que tengamos la base de datos lista
        return True

    def asignar_docente_a_seccion(self):
        
        return True
        #Se terminará de programar despues de que seccion se realice correctamente con un builder

    def asignar_lista_estudiante(self):        
        #Se implementará una vez que tengamos la base de datos lista
        return True
        
    def ver_perfil(self):
        perfil = {
            "Cédula": self.cedula,
            "Nombre Completo": self.obtener_nombre_completo(),
            "Correo": self._correo,
            "ID Coordinador": self.id_coordinador,
            "Fecha de Asignación al Cargo": self.fecha_asignacion_cargo
        }
        return perfil