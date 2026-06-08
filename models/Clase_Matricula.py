class Matricula:
    def __init__(self, idMatricula, tipoMaticula, fechaMatricula, estadoPagoMatricula, costeMatricula):
        self._idMatricula = idMatricula
        self._tipoMatricula = tipoMaticula
        self._fechaMatricula = fechaMatricula
        self.__estadoPagoMatricula = estadoPagoMatricula
        self.costeMatricula = costeMatricula

        #actualmente esta clase no cuenta con métodos, solo pondre algo que me retorne el id y valor de la matricula
    def obtener_id_matricula(self):
        return f"{self._idMatricula}"

    def obtener_coste_matricula(self):
        return f"{self.costeMatricula}"