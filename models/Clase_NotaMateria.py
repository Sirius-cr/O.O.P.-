from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria
from models.Clase_Materia import Materia

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
        #Aqui tambien se deberá colocar una validación, si el estado del periodo aun no se cierra por el coordinador, el esta_aprobado estará en estado pendiente, caso contrario se evaluará si el estudiante aprobó o no la materia, dependiendo de su nota final y asistencia.

        if self.nota_final >= EstadoDeAprobacionMateria.NOTA_MINIMA_APROBACION.value and self.asistencia >= EstadoDeAprobacionMateria.ASISTENCIA_MINIMA.value:
            return EstadoDeAprobacionMateria.MATERIA_APROBADA
        else:
            return EstadoDeAprobacionMateria.MATERIA_REPROBADA

    #Utilizar el archivo Estado_Aprobacion.py para definir los estados de aprobación de la materia y nivelación
