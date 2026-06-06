from abc import ABC, abstractmethod

class GeneradorReportes(ABC):
    @abstractmethod
    def generar_reportes_ministerio(self):
        pass

class RepositorioMinisterio(ABC):
    @abstractmethod
    def guardar_datos(self):
        pass

class BaseDeDatosMinisterio(RepositorioMinisterio):
    def guardar_datos(self):
        print("Datos guardados en la BD del Ministerio")

class Reportes:
    # Cumple DIP: Depende de la abstracción (RepositorioMinisterio)
    def __init__(self, db: RepositorioMinisterio):
        self.db = db

    def enviar_reporte(self):
        self.db.guardar_datos()

        