from models.usuarios.Clases_Usuario import Usuario
from models.academico.Clase_Periodo import Periodo

class UsuarioAdministrativo(Usuario):
    """
    Representa a un Usuario con funciones Administrativas dentro del sistema.
    Hereda de Usuario y permite realizar verificaciones sobre el estado del sistema académico.
    """
    def verificar_estado_sistema(self, periodo: Periodo):
        """
        Consulta el estado de ejecución de un periodo académico específico.

        Parámetros:
        - periodo (Periodo): El periodo a verificar.

        Retorna:
        - str: El estado actual del periodo (e.g., 'Activo', 'Cerrado').
        """
        estado_actual = periodo.estado_periodo
        #f"El sistema se encuentra en estado: {estado_actual}"
        return estado_actual #En la interfaz se colocará el mensaje