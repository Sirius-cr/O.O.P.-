from enum import Enum

class EstadoDeAprobacionMateria(Enum):
    NOTA_MINIMA_APROBACION = 7.0
    ASISTENCIA_MINIMA = 70
    MATERIA_APROBADA = 'Aprobado'
    MATERIA_REPROBADA = 'Reprobado'
    
class EstadoDeAprobacionNivelacion(Enum):
    APROBADO = '' #Recorre los estados de cada materia, si todos son 'Aprobado', estaAprobado = APROBADO (nombre de esta linea), caso contrario REPROBADO
    REPROBADO = ''