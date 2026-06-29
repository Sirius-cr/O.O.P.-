from abc import ABC, abstractmethod
from models.enums.Estado_Aprobacion import EstadoDeAprobacionNivelacion, EstadoDeAprobacionMateria
from models.gestion.Clase_NotaMateria import NotaMateria

class Observador(ABC):
    @abstractmethod
    def actualizar(self):
        pass

# Tu clase modificada
class HistorialAcademico(Observador):
    def __init__(self, id_historial: str):
        self.id_historial = id_historial
        self.lista_nota_materia = []
        self.estado_nivelacion_actual = EstadoDeAprobacionNivelacion.PENDIENTE

    # AHORA RECIBE EL OBJETO PERIODO DESDE DONDE SE MANEJA LA MATRÍCULA
    def crear_nota_materia(self, materia, periodo, parcial1=0.0, parcial2=0.0, asistencia=0):
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
        if not self.lista_nota_materia:
            return 0.0
        suma_notas = sum(nota.nota_final for nota in self.lista_nota_materia)
        return suma_notas / len(self.lista_nota_materia)

    def verificar_aprobacion_nivelacion(self):
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

    # EL TRIGGER AUTOMÁTICO DEL OBSERVER
    def actualizar(self):
        self.estado_nivelacion_actual = self.verificar_aprobacion_nivelacion()
        print(f"--> [OBSERVER] Historial '{self.id_historial}' se ha auto-calculado:")
        print(f"    Promedio General Actual: {self.promedio_general:.2f}")
        print(f"    Estado de Nivelación: {self.estado_nivelacion_actual.value}\n")