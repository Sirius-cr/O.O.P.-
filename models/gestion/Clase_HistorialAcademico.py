from models.enums.Estado_Aprobacion import EstadoDeAprobacionNivelacion, EstadoDeAprobacionMateria
from models.gestion.Clase_NotaMateria import NotaMateria

class HistorialAcademico:
    def __init__(self, id_historial: str):
        self.id_historial = id_historial
        self.lista_nota_materia = []  # Contiene objetos NotaMateria

    def crear_nota_materia(self, materia, parcial1=0.0, parcial2=0.0, asistencia=0):
        nota = NotaMateria(materia=materia, parcial1=parcial1, parcial2=parcial2, asistencia=asistencia, historial=self)
        self.lista_nota_materia.append(nota)
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
            estado_materia = nota.esta_aprobado  # Llama a la property de NotaMateria
            
            if estado_materia == EstadoDeAprobacionMateria.MATERIA_PENDIENTE:
                tiene_materias_pendientes = True
            elif estado_materia == EstadoDeAprobacionMateria.MATERIA_REPROBADA:
                return EstadoDeAprobacionNivelacion.REPROBADO 

        if tiene_materias_pendientes:
            return EstadoDeAprobacionNivelacion.PENDIENTE
        return EstadoDeAprobacionNivelacion.APROBADO
    #Implementar logica que determine que si todas las materias tienen estadoAprobacion = True (esto se encuentra en notaMateria), entonces se retornará True, caso contrario False