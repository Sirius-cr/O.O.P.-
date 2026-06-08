from models.enums.Estado_Aprobacion import EstadoDeAprobacion

class NotaMateria:

    def __init__(self, parcial1, parcial2, asistencia):
        self.parcial1 = parcial1
        self.parcial2 = parcial2
        self.asistencia = asistencia
        self.nota_final = self.calcular_nota_final()

    def calcular_nota_final(self):
        return (self.parcial1 + self.parcial2) / 2

    def esta_aprobado(self):
        return (
            self.nota_final >= EstadoDeAprobacion.NOTA_MINIMA_APROBACION
            and self.asistencia >= EstadoDeAprobacion.ASISTENCIA_MINIMA
        )

    
