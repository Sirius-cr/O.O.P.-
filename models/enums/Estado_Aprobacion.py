from enum import Enum

class EstadoDeAprobacionMateria(Enum):
    NOTA_MINIMA_APROBACION = 7.0
    ASISTENCIA_MINIMA = 70
    MATERIA_APROBADA = 'Materia aprobada'
    MATERIA_REPROBADA = 'Materia reprobada'
    MATERIA_PENDIENTE = 'Materia pendiente'

class EstadoDeAprobacionNivelacion(Enum):
    APROBADO = 'Nivelación Aprobada' #Recorre los estados de cada materia, si todos son 'Aprobado', estaAprobado = APROBADO (nombre de esta linea), caso contrario REPROBADO
    REPROBADO = 'Nivelación Reprobada'
    PENDIENTE = 'Nivelación Pendiente'