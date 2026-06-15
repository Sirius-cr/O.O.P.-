class AulaVirtual:
    def __init__(self, capacidad_maxima, enlace_plataforma, tipo_plataforma):
        self.capacidad_maxima = capacidad_maxima
        self._enlace_plataforma = enlace_plataforma
        self._tipo_plataforma = tipo_plataforma
    
    def obtener_acceso(self):
        return True
