from models.usuarios.Clase_UsuarioAdministrativo import UsuarioAdministrativo
from models.Clase_Reporte import Reporte

class Secretaria(UsuarioAdministrativo):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, idSecretaria, moduloAsignado):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self._idSecretaria = idSecretaria
        self.moduloAsignado = moduloAsignado
        
    def emitirCertificado(self):
        print("Generando y emitiendo certificado académico para el estudiante...")
        return True

    def generarReporte(self, formatoDocumento):
        contenido = (
            f"ID Secretaria:  {self._idSecretaria}\n"
            f"Módulo:         {self.moduloAsignado}\n"
            f"Acción:         Reporte de trámites de secretaría general."
        )
        return Reporte("Reporte de Secretaría", formatoDocumento, self.obtener_nombre_completo(), contenido)
    
#Secretaria tiene el metodo verificarEstadoSistema heredado de UsuarioAdministrativo.
    #ta weno