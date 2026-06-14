from models.usuarios.Clases_Usuario import Usuario
from models.Clase_Periodo import Periodo

class UsuarioAdministrativo(Usuario):
    def verificar_estado_sistema(self, periodo: Periodo):
        estado_actual = periodo.estado_periodo
        #f"El sistema se encuentra en estado: {estado_actual}"
        return estado_actual #En la interfaz se colocará el mensaje