from Clase_Entorno_Academico import EntornoAcademico
class AulaVirtual(EntornoAcademico):
    def __init__(self,identificadorEntorno,capacidadMaxima,tipoPlataforma):
        super().__init__(identificadorEntorno,capacidadMaxima)
        self.tipoPlataforma=tipoPlataforma
    
    def obtenerAcceso(self):
        return print("Acceso a la plataforma:", self.tipoPlataforma)
#composicion con <<interfaz>> con la clase de Materia
