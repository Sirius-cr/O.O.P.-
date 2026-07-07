from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico
from models.gestion.Clase_HistorialAcademico import HistorialAcademico, Observador
from models.patrones_diseno.strategy.ReporteStrategy import Reporte

class Estudiante(UsuarioAcademico, Observador):
    """
    Representa a un Estudiante dentro del sistema.
    Hereda de UsuarioAcademico e implementa la interfaz Observador para recibir notificaciones
    sobre cambios de calificaciones. Gestiona su inscripción en secciones, historial académico,
    reportes de retiro y solicitudes de certificados.
    """
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, id_estudiante, nombre_periodo, tipo_matricula):
        """
        Inicializa una nueva instancia de la clase Estudiante.

        Parámetros:
        - cedula (str): Cédula de identidad del estudiante.
        - nombres (str): Nombres del estudiante.
        - apellidos (str): Apellidos del estudiante.
        - correo (str): Correo electrónico institucional.
        - contrasenia (str): Contraseña de acceso al sistema.
        - id_estudiante (str): Identificador único del estudiante.
        - nombre_periodo (str): Nombre del periodo académico en curso (e.g., 'Nivelacion 2026').
        - tipo_matricula (str): Tipo de matrícula (e.g., 'Ordinaria', 'Extraordinaria').
        """
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self._id_estudiante = id_estudiante
        self.nombre_periodo = nombre_periodo
        self._tipo_matricula = tipo_matricula
        self.historial = HistorialAcademico(id_historial=id_estudiante, estudiante=self)  # Cada estudiante tiene un historial académico asociado
        self.secciones_asociadas = []
        self._archivo_origen = "estudiantes.json"
        self.notificaciones = []
        self.esta_activo = 1

    def inscribir_seccion(self, secciones_asociadas):
        """
        Inscribe al estudiante en una sección académica específica.

        Parámetros:
        - secciones_asociadas (Seccion): La sección en la cual se inscribirá.
        """
        if secciones_asociadas not in self.secciones_asociadas:
            self.secciones_asociadas.append(secciones_asociadas)
            secciones_asociadas.actualizar_estudiantes_inscritos(self)

    @property
    def esta_aprobado(self):
        """
        Propiedad que indica si el estudiante ha aprobado la nivelación actual.

        Retorna:
        - bool: True si está aprobado, False en caso contrario.
        """
        return self.historial.estado_nivelacion_actual
    
    @property
    def tipo_matricula(self):
        """
        Propiedad para obtener el tipo de matrícula del estudiante.
        """
        return self._tipo_matricula

    @property
    def estado_matricula(self):
        """
        Propiedad para obtener el estado de la matrícula del estudiante.
        """
        return "Activa" if self.esta_activo else "Inactiva"

    def actualizar(self, cambio=None, valor=None, nota=None, **kwargs):
        """
        Método de actualización del patrón Observer. Recibe notificaciones
        de cambios en las calificaciones y las registra en la lista de notificaciones.

        Parámetros:
        - cambio (str): Nombre de la calificación cambiada (e.g., 'parcial1').
        - valor (float/int): Nuevo valor asignado a la calificación.
        - nota (NotaMateria): Objeto nota que contiene la materia correspondiente.
        - kwargs (dict): Argumentos con información adicional (e.g., 'autor' del cambio).
        """
        import time
        autor = kwargs.get('autor', 'Un docente')
        if nota and cambio:
            traducciones = {
                "parcial1": "Parcial 1",
                "parcial2": "Parcial 2",
                "asistencia": "Asistencia"
            }
            nombre_cambio = traducciones.get(cambio, cambio)
            valor_formateado = f"{valor}%" if cambio == "asistencia" else f"{valor:.2f}"
            
            mensaje = (
                f"El docente {autor} actualizó la nota en la materia "
                f"{nota.materia.nombre_materia}: {nombre_cambio} ahora es {valor_formateado}."
            )
            
            self.notificaciones.append({
                "mensaje": mensaje,
                "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                "leido": False
            })
            print(f"--> [OBSERVER] Estudiante '{self._id_estudiante}' notificado del cambio en {nombre_cambio}.")
    
    def ver_rendimiento(self):
        """
        Obtiene el peor rendimiento académico del estudiante (su peor calificación).

        Retorna:
        - Nota/float: La peor calificación del estudiante registrada en su historial.
        """
        return self.historial.obtener_peor_nota() #este metodo se definirá en la clase HistorialAcademico para obtener la peor nota del estudiante en los parciales

    def ver_perfil(self):
        """
        Retorna los datos clave del perfil del estudiante en forma de diccionario.

        Retorna:
        - dict: Un diccionario con cédula, nombre, correo, estado y tipo de matrícula.
        """
        perfil = {
            "Cédula": self.cedula,
            "Nombre Completo": self.obtener_nombre_completo(),
            "Correo": self._correo,
            "Estado de Matrícula": self.estado_matricula,
            "Tipo de Matrícula": self.tipo_matricula
        }
        return perfil

    def solicitar_certificado(self, formato_documento="Consola"):
        """
        Genera una solicitud de certificado de estudios oficiales para el estudiante.

        Parámetros:
        - formato_documento (str): Formato deseado del reporte final (e.g. 'Consola', 'PDF').

        Retorna:
        - Reporte: Instancia del reporte con la solicitud.
        """
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
        """
        Retorna el objeto HistorialAcademico del estudiante.

        Retorna:
        - HistorialAcademico: El historial de asignaturas y notas.
        """
        return self.historial

    def solicitar_retiro(self, motivo, formato_documento="Consola"):
        """
        Genera una solicitud formal de retiro del ciclo académico actual por motivos especificados.

        Parámetros:
        - motivo (str): Razón por la cual se solicita el retiro.
        - formato_documento (str): Formato del reporte de retiro.

        Retorna:
        - Reporte: Instancia del reporte con la solicitud de retiro.
        """
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