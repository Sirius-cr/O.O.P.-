from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria
from models.enums.Estado_Aprobacion import ReglasDeAprobacion
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
        if self.historial is not None:
        # Le preguntamos al historial si su periodo correspondiente sigue activo
            if self.historial.estado_periodo == EstadoPeriodo.EN_CURSO.value:
                return EstadoDeAprobacionMateria.PENDIENTE

        # Aplicamos la separación de reglas de negocio que hicimos antes
        if self.nota_final >= ReglasDeAprobacion.NOTA_MINIMA and self.asistencia >= ReglasDeAprobacion.ASISTENCIA_MINIMA:
            return EstadoDeAprobacionMateria.APROBADA
        else:
            return EstadoDeAprobacionMateria.REPROBADA

    #Utilizar el archivo Estado_Aprobacion.py para definir los estados de aprobación de la materia y nivelación
