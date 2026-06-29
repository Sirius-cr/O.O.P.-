from abc import ABC, abstractmethod
import json

# 1. INTERFAZ ESTRATEGIA (Strategy)
class IEstrategiaReporte(ABC):
    @abstractmethod
    def generar(self, tipo_de_reporte: str, emisor: str, contenido: str) -> str:
        pass

# 2. ESTRATEGIA CONCRETA: Consola / Texto Plano
class ReporteConsola(IEstrategiaReporte):
    def generar(self, tipo_de_reporte: str, emisor: str, contenido: str) -> str:
        borde = "=" * 50
        return (
            f"\n{borde}\n"
            f"               REPORTE ACADÉMICO ULEAM - PDF \n"
            f"{borde}\n"
            f"Tipo de Reporte: {tipo_de_reporte}\n"
            f"Formato:         Consola / Texto Plano\n"
            f"Generado por:    {emisor}\n"
            f"{borde}\n"
            f"Contenido:\n"
            f"{contenido}\n"
            f"{borde}\n"
        )

# 3. ESTRATEGIA CONCRETA: JSON 
class ReporteJSON(IEstrategiaReporte):
    def generar(self, tipo_de_reporte: str, emisor: str, contenido: str) -> str:
        documento = {
            "institucion": "ULEAM",
            "tipo_de_reporte": tipo_de_reporte,
            "formato": "JSON",
            "emisor": emisor,
            "contenido": contenido
        }
        return json.dumps(documento, indent=4, ensure_ascii=False)

# 4. EL CONTEXTO (Mantiene compatibilidad con la app)
class Reporte:
    def __init__(self, tipo_de_reporte, formato_documento, emisor, contenido):
        self.tipo_de_reporte = tipo_de_reporte
        self.formato_documento = formato_documento
        self.emisor = emisor
        self.contenido = contenido
        
        # Asigna la estrategia inicial según el formato solicitado
        if formato_documento.upper() == 'JSON':
            self.estrategia = ReporteJSON()
        else:
            self.estrategia = ReporteConsola()

    def cambiar_estrategia(self, nueva_estrategia: IEstrategiaReporte):
        self.estrategia = nueva_estrategia

    def imprimir_reporte(self) -> str:
        return self.estrategia.generar(self.tipo_de_reporte, self.emisor, self.contenido)
