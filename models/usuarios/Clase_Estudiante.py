from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico
from models.gestion.Clase_HistorialAcademico import HistorialAcademico

class Estudiante(UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, id_estudiante, nombre_periodo, estado_matricula, tipo_matricula):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)

        self._id_estudiante = id_estudiante
        self.nombre_periodo = nombre_periodo
        self.estado_matricula = estado_matricula
        self.tipo_matricula = tipo_matricula
        self.historial = HistorialAcademico(id_historial=id_estudiante)  # Cada estudiante tiene un historial académico asociado
        self.secciones = []

    def inscribir_seccion(self, seccion):
        if seccion not in self.secciones:
            self.secciones.append(seccion)
            seccion.actualizar_estudiantes_inscritos(self)

    @property
    def esta_aprobado(self):
        return self.historial.verificar_aprobacion_nivelacion()

    def ver_horario(self):
        return []

    def solicitar_certificado(self):
        return True

    def obtener_historial_academico(self):
        return []

    def solicitar_retiro(self):
        return True

    def __realizar_pago_matricula(self) -> bool:
        return True