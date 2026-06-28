from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria
from models.academico.Clase_Materia import Materia
from models.enums.Estado_Periodo import EstadoPeriodo

class NotaMateria:
    def __init__(self, materia: Materia, parcial1 = 0.0 , parcial2 = 0.0, asistencia = 0, historial = None):
        self.materia = materia
        self.parcial1 = parcial1
        self.parcial2 = parcial2
        self.asistencia = asistencia
        self.historial = historial

        if self.materia:
            if self not in self.materia.notas_materia:
                self.materia.notas_materia.append(self)

    @property
    def nota_final(self):
        return (self.parcial1 + self.parcial2) / 2

    @property
    def esta_aprobado(self):
    # Si no hay historial o el período NO ha finalizado, la materia queda pendiente
        if self.historial is None or self.historial.estado_periodo != EstadoPeriodo.FINALIZADO.value:
            return EstadoDeAprobacionMateria.PENDIENTE

    # Si el período ya finalizó, aplicamos las reglas de negocio con tus constantes
        if self.nota_final >= EstadoDeAprobacionMateria.NOTA_MINIMA_APROBACION.value and self.asistencia >= EstadoDeAprobacionMateria.ASISTENCIA_MINIMA.value:
            return EstadoDeAprobacionMateria.MATERIA_APROBADA
        else:
            return EstadoDeAprobacionMateria.MATERIA_REPROBADA

    #Utilizar el archivo Estado_Aprobacion.py para definir los estados de aprobación de la materia y nivelación
