from models.enums.Estado_Aprobacion import EstadoDeAprobacionNivelacion, EstadoDeAprobacionMateria
from models.Clase_NotaMateria import NotaMateria

class HistorialAcademico:
    def __init__(self, idHistorial: str):
        self.idHistorial = idHistorial
        self.listaNotaMateria = []  # Contiene objetos NotaMateria

    def crearNotaMateria(self, materia, parcial1=0.0, parcial2=0.0, asistencia=0):
        # Composición: El historial crea internamente la calificación
        nota = NotaMateria(materia=materia, parcial1=parcial1, parcial2=parcial2, asistencia=asistencia, historial=self)
        self.listaNotaMateria.append(nota)
        return nota

    @property
    def promedioGeneral(self):
        if not self.listaNotaMateria:
            return 0.0
        suma_notas = sum(nota.notaFinal for nota in self.listaNotaMateria)
        return suma_notas / len(self.listaNotaMateria)

    def verificarAprobacionNivelacion(self):
        if not self.listaNotaMateria:
            return EstadoDeAprobacionNivelacion.PENDIENTE

        tiene_materias_pendientes = False

        # Recorremos los estados de cada materia individual
        for nota in self.listaNotaMateria:
            estado_materia = nota.estaAprobado  # Llama a la property de NotaMateria
            
            if estado_materia == EstadoDeAprobacionMateria.MATERIA_PENDIENTE:
                tiene_materias_pendientes = True
            elif estado_materia == EstadoDeAprobacionMateria.MATERIA_REPROBADA:
                # Caso contrario: con una sola que repruebe, toda la nivelación se reprueba
                return EstadoDeAprobacionNivelacion.REPROBADO 

        # Si no hubo ninguna reprobada, pero hay alguna pendiente, la nivelación sigue pendiente
        if tiene_materias_pendientes:
            return EstadoDeAprobacionNivelacion.PENDIENTE
            
        # Si salimos limpios del bucle (todas están como MATERIA_APROBADA)
        return EstadoDeAprobacionNivelacion.APROBADO
    #Implementar logica que determine que si todas las materias tienen estadoAprobacion = True (esto se encuentra en notaMateria), entonces se retornará True, caso contrario False