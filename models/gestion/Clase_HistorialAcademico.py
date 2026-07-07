from abc import ABC, abstractmethod
from models.enums.Estado_Aprobacion import EstadoDeAprobacionNivelacion, EstadoDeAprobacionMateria
from models.gestion.Clase_NotaMateria import NotaMateria

class Observador(ABC):
    """
    Clase abstracta (Interfaz) para el patrón Observer.
    Define el método actualizar que deben implementar los observadores.
    """
    @abstractmethod
    def actualizar(self, cambio=None, valor=None, nota=None, **kwargs):
        """
        Método a ejecutar cuando el sujeto notifica un cambio.
        """
        pass

class HistorialAcademico(Observador):
    """
    Representa el historial académico de un estudiante.
    Mantiene un registro de las notas por materia y calcula el promedio y estado de aprobación de la nivelación.
    Actúa como observador de los cambios en las notas individuales.
    """
    def __init__(self, id_historial: str, estudiante=None):
        """
        Inicializa un nuevo Historial Académico.

        Parámetros:
        - id_historial (str): Identificador único del historial (usualmente ID del estudiante).
        - estudiante (Estudiante, opcional): Estudiante asociado a este historial.
        """
        self.id_historial = id_historial
        self.estudiante = estudiante
        self.lista_nota_materia = []  # Lista que contiene objetos NotaMateria del estudiante
        self.estado_nivelacion_actual = EstadoDeAprobacionNivelacion.PENDIENTE

    def crear_nota_materia(self, materia, periodo, parcial1=0.0, parcial2=0.0, asistencia=0):
        """
        Crea e inscribe una nueva nota de materia para el periodo actual.

        Parámetros:
        - materia (Materia): Objeto materia correspondiente.
        - periodo (Periodo): Periodo académico en el que se cursa.
        - parcial1 (float): Calificación del primer parcial.
        - parcial2 (float): Calificación del segundo parcial.
        - asistencia (int): Porcentaje o número de asistencias registradas.

        Retorna:
        - NotaMateria: El objeto de nota creado y anexado.
        """
        nota = NotaMateria(
            materia=materia, 
            periodo=periodo, 
            parcial1=parcial1, 
            parcial2=parcial2, 
            asistencia=asistencia, 
            historial=self
        )
        self.lista_nota_materia.append(nota)
        self.actualizar()  # Evaluamos el estado inicial de la nivelación
        return nota

    @property
    def promedio_general(self):
        """
        Propiedad que calcula el promedio general de todas las materias inscritas en el historial.

        Retorna:
        - float: Promedio general de las notas finales.
        """
        if not self.lista_nota_materia:
            return 0.0
        suma_notas = sum(nota.nota_final for nota in self.lista_nota_materia)
        return suma_notas / len(self.lista_nota_materia)

    def verificar_aprobacion_nivelacion(self):
        """
        Verifica el estado actual de aprobación de la nivelación analizando cada materia.
        - Si hay al menos una materia reprobada, el estado general es REPROBADO.
        - Si hay materias pendientes de finalizar, el estado general es PENDIENTE.
        - Si todas las materias están aprobadas, el estado general es APROBADO.

        Retorna:
        - EstadoDeAprobacionNivelacion: El estado correspondiente.
        """
        if not self.lista_nota_materia:
            return EstadoDeAprobacionNivelacion.PENDIENTE

        tiene_materias_pendientes = False

        for nota in self.lista_nota_materia:
            estado_materia = nota.esta_aprobado  
            
            if estado_materia == EstadoDeAprobacionMateria.MATERIA_PENDIENTE:  
                tiene_materias_pendientes = True
            elif estado_materia == EstadoDeAprobacionMateria.MATERIA_REPROBADA:
                return EstadoDeAprobacionNivelacion.REPROBADO 

        if tiene_materias_pendientes:
            return EstadoDeAprobacionNivelacion.PENDIENTE
        return EstadoDeAprobacionNivelacion.APROBADO

    def actualizar(self, cambio=None, valor=None, nota=None, **kwargs):
        """
        Método de actualización del patrón Observer. Reacciona a cambios en las notas
        de materias individuales y recalcula el estado general del periodo.
        """
        self.estado_nivelacion_actual = self.verificar_aprobacion_nivelacion()
        print(f"--> [OBSERVER] Historial '{self.id_historial}' se ha auto-calculado:")
        print(f"    Promedio General Actual: {self.promedio_general:.2f}")
        print(f"    Estado de Nivelación: {self.estado_nivelacion_actual.value}\n")