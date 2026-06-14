from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico
from models.Clase_HistorialAcademico import HistorialAcademico

class Estudiante(UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, idEstudiante, nombrePeriodo, estadoMatricula, tipoMatricula):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)

        self._idEstudiante = idEstudiante
        self.nombrePeriodo = nombrePeriodo
        self.estadoMatricula = estadoMatricula
        self.tipoMatricula = tipoMatricula
        self.historial = HistorialAcademico(idHistorial=idEstudiante)  # Cada estudiante tiene un historial académico asociado

    @property
    def estaAprobado(self):
        return self.historial.verificarAprobacionNivelacion()

    def verHorario(self): # Mapea a +verHorario(). Permite al estudiante revisar su horario de clases.
        #print(f"Cargando el horario de clases para el estudiante {self._nombres}...")
        return [] # Se desarrollará posteriormente para devolver una lista de clases programadas.

    def solicitarCertificado(self):
        #print("Solicitud de certificado académico enviada a secretaría...")
        #Llama al metodo verificarAprobacionNivelacion() del historial académico. Deberá implementarse la lógica en el archivo HistorialAcademico.py, si retorna True el metodo verificarAprobacionNivelacion(), se solicita el certificado, caso contrario se muestra un mensaje indicando que no se puede solicitar el certificado por no haber aprobado la nivelación.
        return True

    def obtenerHistorialAcadémico(self):
        #print("Consultando el registro histórico de calificaciones...")
        return []

    def solicitarRetiro(self):
        #print("Generando solicitud formal de retiro de la nivelación...")
        return True

    def __realizarPagoMatricula(self) -> bool:
        #print("Procesando pago de matrícula en la pasarela interna...")
        return True