class HistorialAcademico:
    def __init__(self, idHistorial):
        self.idHistorial = idHistorial
        self.promedio = 0
        self.listaNotaMateria = []

    def agregarNotaMateria(self, notaMateria):
        self.listaNotaMateria.append(notaMateria)

    def calcularPromedioGeneral(self):

        if len(self.listaNotaMateria) == 0:
            self.promedio = 0
            return self.promedio

        suma = 0

        for nota in self.listaNotaMateria:
            suma += nota.notaFinal

        self.promedio = suma / len(self.listaNotaMateria)

        return self.promedio

    def verificarAprobacionNivelacion(self):

        for nota in self.listaNotaMateria:
            if not nota.estadoAprobacion:
                return False

        return True