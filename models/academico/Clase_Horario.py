from models.academico.Clase_Seccion import Seccion

class Horario:
    """
    Representa el horario asignado a una sección académica.
    Define el turno, la hora de inicio y fin, la modalidad y los días de clase.
    """

    def __init__(self, turno, hora_inicio, hora_fin, modalidad, dias=None):
        """
        Inicializa una nueva instancia de la clase Horario.

        Parámetros:
        - turno (str): Turno del horario (ej. "Mañana", "Tarde", "Noche").
        - hora_inicio (str): Hora de inicio en formato "HH:MM".
        - hora_fin (str): Hora de finalización en formato "HH:MM".
        - modalidad (str): Modalidad de la clase (ej. "Presencial", "Virtual").
        - dias (list, opcional): Lista de días en los que se dicta la clase. Por defecto ["Lunes", "Miércoles", "Viernes"].
        """
        self.turno = turno
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self._modalidad = modalidad  # Atributo protegido para almacenar la modalidad
        self.dias = dias if dias is not None else ["Lunes", "Miércoles", "Viernes"]
    
    def deteccion_colision(self, otro_horario):
        """
        Detecta si existe una colisión (traslape) de horarios con otro objeto Horario.

        Compara los días en común y si los intervalos de tiempo se superponen.

        Parámetros:
        - otro_horario (Horario): El otro horario con el cual comparar.

        Retorna:
        - bool: True si hay colisión (traslape de días y horas), False en caso contrario.
        """
        def a_minutos(hora_str):
            """Convierte una cadena de hora 'HH:MM' a minutos desde el inicio del día."""
            try:
                h, m = map(int, hora_str.split(':'))
                return h * 60 + m
            except:
                return 0

        # Convierte las horas de inicio y fin a minutos para facilitar la comparación
        inicio1 = a_minutos(self.hora_inicio)
        fin1 = a_minutos(self.hora_fin)
        inicio2 = a_minutos(otro_horario.hora_inicio)
        fin2 = a_minutos(otro_horario.hora_fin)

        # Encuentra los días que coinciden entre ambos horarios
        dias_en_comun = set(self.dias).intersection(set(otro_horario.dias))
        
        # Si comparten al menos un día, verifica si hay traslape de horas
        if dias_en_comun:
            if max(inicio1, inicio2) < min(fin1, fin2):
                return True
        return False

    def resumen_de_seccion(self, Seccion: Seccion):
        """
        Genera un resumen detallado de la sección vinculada con este horario.

        Parámetros:
        - Seccion (Seccion): La sección académica asociada.

        Retorna:
        - dict: Un diccionario con los datos del turno, horas, modalidad y docentes asignados.
        """
        # Verifica si la sección cuenta con docentes asignados
        if Seccion.docentes:
            docentes_nombres = Seccion.docentes
        else:
            print("Sin docentes asignado")
            docentes_nombres = None

        return {
            "Turno": self.turno,
            "Inicio": self.hora_inicio,
            "Fin": self.hora_fin,
            "Modalidad": self._modalidad,
            "Docente": docentes_nombres
        }


    