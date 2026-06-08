from models.usuarios.Clase_UsuarioAdministrativo import UsuarioAdministrativo

class Secretaria(UsuarioAdministrativo):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, idSecretaria, moduloAsignado):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self._idSecretaria = idSecretaria
        self.moduloAsignado = moduloAsignado
        
    def emitirCertificado(self):
        print("Generando y emitiendo certificado académico para el estudiante...")
        return True
    
#Secretaria tiene el metodo verificarEstadoSistema heredado de UsuarioAdministrativo.