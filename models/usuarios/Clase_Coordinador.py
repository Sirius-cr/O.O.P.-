from models.usuarios.Clase_UsuarioAdministrativo import UsuarioAdministrativo
from models.academico.Clase_Periodo import Periodo
from models.patrones_diseno.strategy.ReporteStrategy import Reporte

class Coordinador(UsuarioAdministrativo):
    """
    Representa a un Coordinador dentro del sistema.
    Hereda de UsuarioAdministrativo y se encarga de la gestión académica de carreras,
    secciones, periodos de matrícula y asignación de docentes.
    """
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, id_coordinador, fecha_asignacion_cargo):
        """
        Inicializa una nueva instancia de la clase Coordinador.

        Parámetros:
        - cedula (str): Cédula de identidad del coordinador.
        - nombres (str): Nombres del coordinador.
        - apellidos (str): Apellidos del coordinador.
        - correo (str): Correo electrónico institucional.
        - contrasenia (str): Contraseña de acceso al sistema.
        - id_coordinador (str): Identificador único del coordinador.
        - fecha_asignacion_cargo (str): Fecha en la que se le asignó el cargo.
        """
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.id_coordinador = id_coordinador
        self.fecha_asignacion_cargo = fecha_asignacion_cargo
        self.carrera = None
        self.secciones_coordinadas = []

    def asociar_carrera(self, carrera):
        """
        Asocia una carrera específica al coordinador.

        Parámetros:
        - carrera (Carrera): Objeto carrera que coordinará.
        """
        if self.carrera != carrera:
            self.carrera = carrera
            carrera.asociar_coordinador(self)

    def coordinar_seccion(self, seccion):
        """
        Agrega una sección a la lista de secciones coordinadas por este coordinador.

        Parámetros:
        - seccion (Seccion): Sección académica a coordinar.
        """
        if seccion not in self.secciones_coordinadas:
            self.secciones_coordinadas.append(seccion)
            seccion.coordinador = self
        
    def abrir_periodo_matricula(self, periodo: Periodo):
        """
        Permite al coordinador iniciar un periodo de matrícula académica.

        Parámetros:
        - periodo (Periodo): El periodo académico a iniciar.
        
        Retorna:
        - bool: True si la operación se realiza con éxito.
        """
        periodo.iniciar_periodo()
        return True

    def cerrar_periodo_matricula(self, periodo: Periodo):
        """
        Permite al coordinador finalizar/cerrar un periodo de matrícula académica.

        Parámetros:
        - periodo (Periodo): El periodo académico a finalizar.

        Retorna:
        - bool: True si la operación se realiza con éxito.
        """
        periodo.finalizar_periodo()
        return True

    def aprobar_retiro(self):
        """
        Aprueba la solicitud de retiro de un estudiante.
        (Pendiente de implementación con la base de datos).

        Retorna:
        - bool: True por defecto en la simulación.
        """
        #Se implementará una vez que tengamos la base de datos lista
        return True

    def asignar_docente_a_seccion(self):
        """
        Asigna un docente a una sección específica.
        (Pendiente de finalizar la programación tras la implementación de la sección con Builder).

        Retorna:
        - bool: True por defecto.
        """
        return True
        #Se terminará de programar despues de que seccion se realice correctamente con un builder

    def asignar_lista_estudiante(self):        
        """
        Asigna una lista de estudiantes a la coordinación.
        (Pendiente de integración con la base de datos).

        Retorna:
        - bool: True por defecto.
        """
        #Se implementará una vez que tengamos la base de datos lista
        return True
        
    def ver_perfil(self):
        """
        Obtiene y retorna la información detallada del perfil del coordinador.

        Retorna:
        - dict: Un diccionario con los datos del perfil (Cédula, Nombre Completo, Correo, ID, Fecha de asignación).
        """
        perfil = {
            "Cédula": self.cedula,
            "Nombre Completo": self.obtener_nombre_completo(),
            "Correo": self._correo,
            "ID Coordinador": self.id_coordinador,
            "Fecha de Asignación al Cargo": self.fecha_asignacion_cargo
        }
        return perfil

    
    def filtrar_docentes_por_especialidad(self, docentes, especialidad):
        """
        Filtra una lista de docentes devolviendo únicamente aquellos que tienen una especialidad dada.

        Parámetros:
        - docentes (list): Lista de objetos Docente a evaluar.
        - especialidad (str): Especialidad requerida para el filtro.

        Retorna:
        - list: Subconjunto de docentes que cumplen con la especialidad.
        """
        docentes_filtrados = []

        for docente in docentes:
            if especialidad in docente.especialidades:
                docentes_filtrados.append(docente)

        return docentes_filtrados