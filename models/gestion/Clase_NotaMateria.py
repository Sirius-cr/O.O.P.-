from abc import ABC, abstractmethod
from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria
from models.academico.Clase_Materia import Materia
from models.enums.Estado_Periodo import EstadoPeriodo
from models.academico.Clase_Periodo import Periodo

# Interfaces del Patrón Observer
class Sujeto(ABC):
    """
    Clase abstracta que actúa como el Sujeto en el patrón Observer.
    Mantiene una lista de observadores y notifica cambios de estado.
    """
    def __init__(self):
        """Inicializa la lista de observadores vacía."""
        self._observadores = []

    def anexar(self, observador):
        """Añade un observador al sujeto si no se encuentra registrado."""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def remover(self, observador):
        """Elimina un observador de la lista del sujeto."""
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar(self, cambio=None, valor=None, nota=None):
        """Notifica de forma automática a todos los observadores registrados sobre el cambio."""
        autor = getattr(self, 'ultimo_modificador', 'Un docente')
        for observador in self._observadores:
            observador.actualizar(cambio, valor, nota, autor=autor)


class NotaMateria(Sujeto):
    """
    Representa el registro de calificaciones (parciales y asistencia) de un estudiante en una materia específica.
    Implementa la clase Sujeto para notificar automáticamente cambios en las notas al historial académico
    y al estudiante.
    """
    def __init__(self, materia: Materia, periodo: Periodo, parcial1 = 0.0 , parcial2 = 0.0, asistencia = 0, historial = None):
        """
        Inicializa una nueva instancia de la clase NotaMateria.

        Parámetros:
        - materia (Materia): La asignatura académica asociada.
        - periodo (Periodo): El periodo académico en curso.
        - parcial1 (float): Calificación del primer parcial (por defecto 0.0).
        - parcial2 (float): Calificación del segundo parcial (por defecto 0.0).
        - asistencia (int): Asistencias registradas del estudiante.
        - historial (HistorialAcademico): El historial del alumno a vincular como observador.
        """
        super().__init__()
        self.materia = materia
        self.periodo = periodo  # Guardamos el objeto periodo real
        self._parcial1 = parcial1
        self._parcial2 = parcial2
        self._asistencia = asistencia
        self.historial = historial

        # Registra la nota dentro de la lista general de notas de la materia
        if self.materia:
            if self not in self.materia.notas_materia:
                self.materia.notas_materia.append(self)
                
        # Anexa observadores automáticos para reaccionar a cambios en notas
        if self.historial:
            self.anexar(self.historial)
            if hasattr(self.historial, 'estudiante') and self.historial.estudiante:
                self.anexar(self.historial.estudiante)

    # Interceptamos los cambios de notas usando propiedades para notificar a los observadores
    @property
    def parcial1(self): 
        """Retorna la calificación del parcial 1."""
        return self._parcial1

    @parcial1.setter
    def parcial1(self, valor):
        """Establece la calificación del parcial 1 y notifica el cambio."""
        self._parcial1 = valor
        self.notificar("parcial1", valor, self)

    @property
    def parcial2(self): 
        """Retorna la calificación del parcial 2."""
        return self._parcial2

    @parcial2.setter
    def parcial2(self, valor):
        """Establece la calificación del parcial 2 y notifica el cambio."""
        self._parcial2 = valor
        self.notificar("parcial2", valor, self)

    @property
    def asistencia(self): 
        """Retorna el porcentaje de asistencia."""
        return self._asistencia

    @asistencia.setter
    def asistencia(self, valor):
        """Establece el porcentaje de asistencia y notifica el cambio."""
        self._asistencia = valor
        self.notificar("asistencia", valor, self)

    @property
    def nota_final(self):
        """
        Propiedad que calcula la nota final como promedio simple de los dos parciales.
        """
        return (self._parcial1 + self._parcial2) / 2

    @property
    def esta_aprobado(self):
        """
        Determina el estado de aprobación de la materia.
        - Si el periodo no ha finalizado, el estado es PENDIENTE.
        - Si el periodo finalizó, valida que se cumpla la nota mínima y la asistencia mínima.
        """
        # Si el periodo no ha finalizado, el estado es MATERIA_PENDIENTE
        if self.periodo is None or self.periodo.estado_periodo != EstadoPeriodo.FINALIZADO.value:
            return EstadoDeAprobacionMateria.MATERIA_PENDIENTE

        # Si el período ya finalizó, aplicamos las constantes de validación
        if self.nota_final >= EstadoDeAprobacionMateria.NOTA_MINIMA_APROBACION.value and self.asistencia >= EstadoDeAprobacionMateria.ASISTENCIA_MINIMA.value:
            return EstadoDeAprobacionMateria.MATERIA_APROBADA
        else:
            return EstadoDeAprobacionMateria.MATERIA_REPROBADA