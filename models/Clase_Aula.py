from Clase_Entorno_Academico import EntornoAcademico
class Aula(EntornoAcademico):
    def __init__(self,identifiacadoEntorno,capacidadMaxima,ubicacionFisica):
        super().__init__(identifiacadoEntorno,capacidadMaxima)
        self.ubicacionFisica=ubicacionFisica

    def obtenerAcceso(self):
        return print("La Aula fisica esta ubicada en ", self.ubicacionFisica)
    
    def ocultar_horario_lleno(self):
        return print("Horario ocultado por capacidad maxima superada")