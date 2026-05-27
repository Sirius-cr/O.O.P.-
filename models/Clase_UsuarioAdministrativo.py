from Clases_Usuario import Usuario
class UsuarioAdministrativo(Usuario):
    
    def __init__(self, cedula, nombres, apellidos, correo, contrasena, codigo_administrador):
        super().__init__(cedula, nombres, apellidos, correo, contrasena)
        self._codigo_administrador = codigo_administrador
    #aqui nuevamente escribire los metodos de la clase abstracta para que si los herede
    def iniciar_sesion(self):
        return f"Administrador {self.nombres} ha iniciado sesión en el sistema."

    def registrarse(self):
        return "Procesando registro de nuevo usuario administrativo..."

    def recuperar_contrasena(self):
        return f"Enviando enlace de recuperación al correo: {self._correo}"

    # estos ya serian los metodos propios
    def _consultar_bd_ministerio(self):
        return f"base de datos del ministerio conectada"

    def _matricular_postulante(self):
        pass

    def _promover_estudiante(self):
        pass

    def _asignar_docentes(self):
        pass

    def _aprobar_retiro(self):
        pass

    def _consultar_pagos(self):
        pass

    def _enviar_reporte(self):
        pass