from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico
from models.gestion.Clase_HistorialAcademico import HistorialAcademico, Observador
from models.patrones_diseno.strategy.ReporteStrategy import Reporte

class Estudiante(UsuarioAcademico, Observador):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, id_estudiante, nombre_periodo, tipo_matricula):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self._id_estudiante = id_estudiante
        self.nombre_periodo = nombre_periodo
        self._tipo_matricula = tipo_matricula
        self.historial = HistorialAcademico(id_historial=id_estudiante, estudiante=self)  # Cada estudiante tiene un historial académico asociado
        self.secciones_asociadas = []
        self._archivo_origen = "estudiantes.json"
        self.notificaciones = []
        self.esta_activo = 1

    def inscribir_seccion(self, seccion):
        ya_tiene_materia = any(sec.materia.id_materia == seccion.materia.id_materia for sec in self.secciones_asociadas)
        if not ya_tiene_materia:
            msg = seccion.actualizar_estudiantes_inscritos(self)
            if seccion not in self.secciones_asociadas and "correctamente" in msg:
                self.secciones_asociadas.append(seccion)
            return msg
        return "El estudiante ya está inscrito en una sección de esta materia."

    def ver_horario(self):
        horarios_info = []
        for sec in self.secciones_asociadas:
            for hor in sec.lista_horarios:
                resumen = hor.resumen_de_seccion(sec)
                horarios_info.append({
                    "materia": sec.materia.nombre_materia,
                    "seccion": sec.id_seccion,
                    "turno": resumen.get("Turno de clase"),
                    "inicio": resumen.get("Inicializacion"),
                    "fin": resumen.get("Terminacion"),
                    "modalidad": resumen.get("Modalidad"),
                    "docente": resumen.get("Docente"),
                    "dias": hor.dias,
                    "aula": sec.aula_virtual._enlace_plataforma if sec.aula_virtual else None
                })
        return horarios_info

    @property
    def esta_aprobado(self):
        return self.historial.estado_nivelacion_actual
    
    def actualizar(self, cambio=None, valor=None, nota=None, **kwargs):
        import time
        autor = kwargs.get('autor', 'Un docente')
        if nota and cambio:
            print(f"[NOTIFICACIÓN] Estudiante {self.obtener_nombre_completo()} (ID: {self._id_estudiante}) notificado:")
            print(f"    Su calificación '{cambio}' en la materia '{nota.materia.nombre_materia}' ha sido cambiada a: {valor} por {autor}\n")
            
            mensaje = f"El docente {autor} ha modificado tu calificación de {cambio} en '{nota.materia.nombre_materia}' a {valor}."
            self.notificaciones.append({
                "mensaje": mensaje,
                "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                "leido": False
            })
    
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
        return self.historial.lista_nota_materia

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