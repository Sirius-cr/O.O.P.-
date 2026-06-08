class Reporte:
    def __init__(self, tipoDeReporte, formatoDocumento, emisor, contenido):
        self.tipoDeReporte = tipoDeReporte
        self.formatoDocumento = formatoDocumento
        self.emisor = emisor
        self.contenido = contenido

    def imprimirReporte(self):
        borde = "=" * 50
        return (
            f"\n{borde}\n"
            f"               REPORTE ACADÉMICO ULEAM\n"
            f"{borde}\n"
            f"Tipo de Reporte: {self.tipoDeReporte}\n"
            f"Formato:         {self.formatoDocumento}\n"
            f"Generado por:    {self.emisor}\n"
            f"{borde}\n"
            f"Contenido:\n"
            f"{self.contenido}\n"
            f"{borde}\n"
        )
