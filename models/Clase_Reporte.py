class Reporte:
    def __init__(self, tipo_de_reporte, formato_documento, emisor, contenido):
        self.tipo_de_reporte = tipo_de_reporte
        self.formato_documento = formato_documento
        self.emisor = emisor
        self.contenido = contenido

    def imprimir_reporte(self):
        borde = "=" * 50
        return (
            f"\n{borde}\n"
            f"               REPORTE ACADÉMICO ULEAM\n"
            f"{borde}\n"
            f"Tipo de Reporte: {self.tipo_de_reporte}\n"
            f"Formato:         {self.formato_documento}\n"
            f"Generado por:    {self.emisor}\n"
            f"{borde}\n"
            f"Contenido:\n"
            f"{self.contenido}\n"
            f"{borde}\n"
        )
