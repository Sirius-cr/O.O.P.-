from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico

class Estudiante(UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, idEstudiante, nombrePeriodo, estadoNivelacion):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)

        self._idEstudiante = idEstudiante
        self.nombrePeriodo = nombrePeriodo
        self.estadoNivelacion = estadoNivelacion

    def verHorario(self): # Mapea a +verHorario(). Permite al estudiante revisar su horario de clases.
        print(f"Cargando el horario de clases para el estudiante {self._nombres}...")
        return [] # Se desarrollará posteriormente para devolver una lista de clases programadas.

    def solicitarCertificado(self):
        print("Solicitud de certificado académico enviada a secretaría...")
        return True

    def obtenerHistorialAcadémico(self):
        print("Consultando el registro histórico de calificaciones...")
        return []

    def solicitarRetiro(self):
        print("Generando solicitud formal de retiro de la nivelación...")
        return True

    def __realizarPagoMatricula(self) -> bool:
        print("Procesando pago de matrícula en la pasarela interna...")
        return True