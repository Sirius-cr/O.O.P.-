from Clase_Entorno_Academico import EntornoAcademico
class AulaVirtual(EntornoAcademico):
    def __init__(self,identificadorEntorno,capacidadMaxima,enlacePlataforma):
        super().__init__(identificadorEntorno,capacidadMaxima)
        self.enlacePlataforma=enlacePlataforma
    
    def obtenerAcceso(self):
        return "Acceso a la plataforma:", self.enlacePlataforma
#composicion con <<interfaz>> con la clase de Materia
