from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico
from models.gestion.Clase_HistorialAcademico import HistorialAcademico
from models.patrones_diseno.strategy.ReporteStrategy import Reporte

class Estudiante(UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, id_estudiante, nombre_periodo, tipo_matricula):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)

        self._id_estudiante = id_estudiante
        self.nombre_periodo = nombre_periodo
        self._tipo_matricula = tipo_matricula
        self.historial = HistorialAcademico(id_historial=id_estudiante)  # Cada estudiante tiene un historial académico asociado
        self.secciones_asociadas = []

    def inscribir_seccion(self, secciones_asociadas):
        if secciones_asociadas not in self.secciones_asociadas:
            self.secciones_asociadas.append(secciones_asociadas)
            secciones_asociadas.actualizar_estudiantes_inscritos(self)

    @property
    def esta_aprobado(self):
        return self.historial.estado_nivelacion_actual
    
    def ver_rendimiento(self):
        return self.historial.obtener_peor_nota() #este metodo se definirá en la clase HistorialAcademico para obtener la peor nota del estudiante en los parciales

    def ver_perfil(self):
        print(f"NOMBRE : {self.nombres}")
        print(f"APELLIDOS : {self.apellidos}")
        print(f"CEDULA : {self.cedula}")
        print(f"CORREO : {self.correo}")
        #cada usuario puede ver su perfil

    def solicitar_certificado(self, formato_documento="Consola"):
        contenido = (
            f"El estudiante {self.obtener_nombre_completo()} (ID: {self._id_estudiante}) "
            f"solicita un certificado de estudios oficiales para el periodo {self.nombre_periodo}."
        )
        return Reporte(
            tipo_de_reporte="Solicitud de Certificado",
            formato_documento=formato_documento,
            emisor=self.obtener_nombre_completo(),
            contenido=contenido
        )

    def obtener_historial_academico(self):
        return []

    def solicitar_retiro(self, motivo, formato_documento="Consola"):
        contenido = (
            f"El estudiante {self.obtener_nombre_completo()} (ID: {self._id_estudiante}) "
            f"solicita el retiro del ciclo académico actual por el siguiente motivo: {motivo}."
        )
        return Reporte(
            tipo_de_reporte="Solicitud de Retiro",
            formato_documento=formato_documento,
            emisor=self.obtener_nombre_completo(),
            contenido=contenido
        )