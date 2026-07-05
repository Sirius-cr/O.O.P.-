from abc import ABC, abstractmethod

# 1. EL IMPLEMENTADOR (Streaming Service Interface)
class IServicioStreaming(ABC):
    @abstractmethod
    def crear_reunion(self, nombre_aula: str) -> str:
        pass

# 2. IMPLEMENTADORES CONCRETOS
class ServicioTeams(IServicioStreaming):
    def crear_reunion(self, nombre_aula: str) -> str:
        return f"https://teams.microsoft.com/meet/{nombre_aula.lower()}"

class ServicioZoom(IServicioStreaming):
    def crear_reunion(self, nombre_aula: str) -> str:
        return f"https://zoom.us/j/{nombre_aula.lower()}"


# 3. LA ABSTRACCIÓN (Virtual Classroom Base)
class AulaVirtual:
    def __init__(self, capacidad_maxima, servicio: IServicioStreaming, enlace_personalizado=None):
        self.capacidad_maxima = capacidad_maxima
        self.servicio = servicio  # El PUENTE (Bridge)
        self.enlace_personalizado = enlace_personalizado

    @property
    def _tipo_plataforma(self) -> str:
        # Retorna dinámicamente el nombre de la plataforma según la clase del servicio
        if isinstance(self.servicio, ServicioZoom):
            return "ZOOM"
        return "TEAMS"

    @property
    def _enlace_plataforma(self) -> str:
        # Genera el enlace de forma dinámica usando el servicio de streaming
        if self.enlace_personalizado:
            return self.enlace_personalizado
        return self.servicio.crear_reunion("general")

    def obtener_acceso(self) -> bool:
        return True


# 4. ABSTRACCIONES REFINADAS
class AulaClaseSincrona(AulaVirtual):
    @property
    def _enlace_plataforma(self) -> str:
        # Genera un enlace específico para una clase de teoría sincrónica o retorna el personalizado
        if self.enlace_personalizado:
            return self.enlace_personalizado
        return self.servicio.crear_reunion("clase-teorica")

class AulaExamen(AulaVirtual):
    @property
    def _enlace_plataforma(self) -> str:
        # Genera un enlace específico para un examen o retorna el personalizado
        if self.enlace_personalizado:
            return self.enlace_personalizado
        return self.servicio.crear_reunion("aula-examen-seguro")

