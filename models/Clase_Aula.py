from models.Clase_Entorno_Academico import EntornoAcademico
from abc import ABC

class Aula(EntornoAcademico):
    def __init__(self,identifiacadoEntorno,capacidadMaxima,ubicacionFisica):
        super().__init__(identifiacadoEntorno,capacidadMaxima)
        self.ubicacionFisica=ubicacionFisica

    def obtenerAcceso(self)-> str:
        return f"La Aula fisica esta ubicada en {self.ubicacionFisica}"
    
    @classmethod
    def crear_aula_automaticamente(cls, objeto_carrera, numero_consecutivo: int, capacidad: int, ubicacion: str):
        codigo_corto = objeto_carrera.id_carrera
        identifcador_compuesto = f"Aula-{codigo_corto}-{numero_consecutivo}"
        return cls(identifcador_compuesto, capacidad, ubicacion)