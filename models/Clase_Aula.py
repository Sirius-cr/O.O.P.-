from Clase_Entorno_Academico import EntornoAcademico
class Aula(EntornoAcademico):
    def __init__(self,identifiacadoEntorno,capacidadMaxima,ubicacionFisica):
       super().__init__(identifiacadoEntorno,capacidadMaxima)
       self.ubicacionFisica=ubicacionFisica

    def obtenerAcceso(self):
        return f"La Aula fisica esta ubicada en ", self.ubicacionFisica