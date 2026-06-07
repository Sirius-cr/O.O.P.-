from models.usuarios.Clases_Usuario import Usuario
from models.Clase_Periodo import Periodo

class UsuarioAdministrativo(Usuario):
    def verificarEstadoSistema(self, periodo: Periodo):
        estado_actual = periodo.estado_periodo()
        return f"El sistema se encuentra en estado: {estado_actual}"