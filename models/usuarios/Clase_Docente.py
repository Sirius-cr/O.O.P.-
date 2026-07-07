from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico
from models.patrones_diseno.strategy.ReporteStrategy import Reporte

class Docente(UsuarioAcademico):
    """
    Representa a un Docente dentro del sistema.
    Hereda de UsuarioAcademico y maneja las secciones impartidas, especialidades,
    calificaciones, control de asistencia y generación de reportes.
    """
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, especialidad=None):
        """
        Inicializa una nueva instancia de la clase Docente.

        Parámetros:
        - cedula (str): Cédula de identidad del docente.
        - nombres (str): Nombres del docente.
        - apellidos (str): Apellidos del docente.
        - correo (str): Correo electrónico institucional.
        - contrasenia (str): Contraseña de acceso al sistema.
        - especialidad (str, opcional): Especialidad inicial del docente.
        """
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.secciones = []
        self.especialidades = []
        if especialidad:
            self.especialidades.append(especialidad)

    @property
    def especialidad(self):
        """
        Retorna la especialidad principal del docente (la primera en la lista)
        o 'Sin especialidad' si no tiene ninguna asignada.
        """
        return self.especialidades[0] if self.especialidades else "Sin especialidad"

    def agregar_especialidad(self, especialidad):
        """
        Agrega una nueva especialidad a la lista de especialidades del docente.

        Parámetros:
        - especialidad (str): Nombre de la especialidad (ej. "Matemáticas").
        """
        if especialidad not in self.especialidades:
            self.especialidades.append(especialidad)

    def ver_rendimiento(self):
        """
        Muestra la media académica o el rendimiento general de los estudiantes en la sección a su cargo.
        
        Retorna:
        - str: Mensaje descriptivo con el estado de la sección.
        """
        return "Mostrando rendimiento de los estudiantes en la sección" #aqui se implementará la lógica para mostrar el rendimiento de los estudiantes en la sección que el docente imparte

    def ver_perfil(self):
        """
        Imprime en consola los datos del perfil del docente.
        """
        print(f"NOMBRE : {self.nombres}")
        print(f"APELLIDOS : {self.apellidos}")
        print(f"CORREO : {self.correo}")
        print(f"ESPECIALIDAD : {self.especialidad}")

    def colocar_calificacion(self):
        """
        Permite al docente asignar notas a un estudiante en su sección.
        (Pendiente de implementación con la interacción de Sección y la UI).
        """
        pass #Llama al metodo registrarNotaEstudiante() que se encuentra en seccion, luego se le mostrarán todos los estudiantes que se encuentren en esa seccion, y podra seleccionar al estudiante al que desea colocar la calificacion

    def tomar_asistencia(self):
        """
        Registra la asistencia de los estudiantes en la clase correspondiente.
        """
        return 

    def asignar_seccion(self, seccion):
        """
        Asocia una sección específica a este docente.

        Parámetros:
        - seccion (Seccion): La sección académica asignada.
        """
        if seccion not in self.secciones:
            self.secciones.append(seccion)
            seccion.agregar_docente(self)

    def realizaReporte(self, tipo_de_reporte, formato_documento, contenido):
        """
        Genera un nuevo reporte académico o disciplinario utilizando el patrón Strategy.

        Parámetros:
        - tipo_de_reporte (str): El tipo o título del reporte.
        - formato_documento (str): Formato del reporte (e.g., PDF, Consola).
        - contenido (str): Texto explicativo del reporte.

        Retorna:
        - Reporte: Instancia del reporte generado.
        """
        return Reporte(
            tipo_de_reporte=tipo_de_reporte,
            formato_documento=formato_documento,
            emisor=self.obtener_nombre_completo(),
            contenido=contenido
        )