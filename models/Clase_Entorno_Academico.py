from abc import ABC,abstractclassmethod

class EntornoAcademico(ABC):
    def __init__(self,identificadorEntorno,capacidadMaxima):
        self.identificadorEntorno=identificadorEntorno
        self.capacidadMaxima=capacidadMaxima

    def obtenerAcceso(self):
        pass