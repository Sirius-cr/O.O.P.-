from abc import ABC,abstractmethod

class EntornoAcademico(ABC):
    def __init__(self,identificadorEntorno,capacidadMaxima):
        self.identificadorEntorno=identificadorEntorno
        self.capacidadMaxima=capacidadMaxima
    @abstractmethod
    def obtenerAcceso(self):
        pass