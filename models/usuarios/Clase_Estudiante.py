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

    @property
    def esta_aprobado(self):
        return self.historial.verificar_aprobacion_nivelacion()
    
    def ver_rendimiento(self):
        return self.historial.obtener_peor_nota() #este metodo se definirá en la clase HistorialAcademico para obtener la peor nota del estudiante en los parciales

    def ver_perfil(self):
        perfil = {
            "Cédula": self.cedula,
            "Nombre Completo": self.obtener_nombre_completo(),
            "Correo": self._correo,
            "Estado de Matrícula": self.estado_matricula,
            "Tipo de Matrícula": self.tipo_matricula
        }
        return perfil

    def solicitar_certificado(self):
        return True

    def obtener_historial_academico(self):
        return self.historial

    def solicitar_retiro(self):
        return True