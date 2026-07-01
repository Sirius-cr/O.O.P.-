from abc import ABC, abstractmethod
from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria
from models.academico.Clase_Materia import Materia
from models.enums.Estado_Periodo import EstadoPeriodo
from models.academico.Clase_Periodo import Periodo

# Interfaces del Patrón Observer
class Sujeto(ABC):
    def __init__(self):
        self._observadores = []

    def anexar(self, observador):
        if observador not in self._observadores:
            self._observadores.append(observador)

    def remover(self, observador):
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar(self, cambio=None, valor=None, nota=None):
        autor = getattr(self, 'ultimo_modificador', 'Un docente')
        for observador in self._observadores:
            observador.actualizar(cambio, valor, nota, autor=autor)


class NotaMateria(Sujeto):
    def __init__(self, materia: Materia, periodo: Periodo, parcial1 = 0.0 , parcial2 = 0.0, asistencia = 0, historial = None):
        super().__init__()
        self.materia = materia
        self.periodo = periodo  # Guardamos el objeto periodo real
        self._parcial1 = parcial1
        self._parcial2 = parcial2
        self._asistencia = asistencia
        self.historial = historial

        if self.materia:
            if self not in self.materia.notas_materia:
                self.materia.notas_materia.append(self)
                
        if self.historial:
            self.anexar(self.historial)
            if hasattr(self.historial, 'estudiante') and self.historial.estudiante:
                self.anexar(self.historial.estudiante)

    # Interceptamos los cambios de notas usando propiedades
    @property
    def parcial1(self): return self._parcial1
    @parcial1.setter
    def parcial1(self, valor):
        self._parcial1 = valor
        self.notificar("parcial1", valor, self)  # Avisa automáticamente a todos los observadores

    @property
    def parcial2(self): return self._parcial2
    @parcial2.setter
    def parcial2(self, valor):
        self._parcial2 = valor
        self.notificar("parcial2", valor, self)

    @property
    def asistencia(self): return self._asistencia
    @asistencia.setter
    def asistencia(self, valor):
        self._asistencia = valor
        self.notificar("asistencia", valor, self)

    @property
    def nota_final(self):
        return (self._parcial1 + self._parcial2) / 2

    @property
    def esta_aprobado(self):
        # Si el periodo no ha finalizado, el estado es MATERIA_PENDIENTE
        if self.periodo is None or self.periodo.estado_periodo != EstadoPeriodo.FINALIZADO.value:
            return EstadoDeAprobacionMateria.MATERIA_PENDIENTE  # <-- CORREGIDO

        # Si el período ya finalizó, aplicamos tus constantes exactas
        if self.nota_final >= EstadoDeAprobacionMateria.NOTA_MINIMA_APROBACION.value and self.asistencia >= EstadoDeAprobacionMateria.ASISTENCIA_MINIMA.value:
            return EstadoDeAprobacionMateria.MATERIA_APROBADA
        else:
            return EstadoDeAprobacionMateria.MATERIA_REPROBADA