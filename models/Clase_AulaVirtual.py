class AulaVirtual:
    def __init__(self,capacidadMaxima,enlacePlataforma, tipoPlataforma):
        self.capacidadMaxima = capacidadMaxima
        self._enlacePlataforma=enlacePlataforma
        self._tipoPlataforma=tipoPlataforma
    
    def obtenerAcceso(self):
        return True
