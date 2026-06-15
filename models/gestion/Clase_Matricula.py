class Matricula:
    def __init__(self, id_matricula, tipo_matricula, fecha_matricula, estado_pago_matricula, coste_matricula):
        self._id_matricula = id_matricula
        self._tipo_matricula = tipo_matricula
        self._fecha_matricula = fecha_matricula
        self.__estado_pago_matricula = estado_pago_matricula
        self.coste_matricula = coste_matricula

        #actualmente esta clase no cuenta con métodos, solo pondre algo que me retorne el id y valor de la matricula
    def obtener_id_matricula(self):
        return f"{self._id_matricula}"

    def obtener_coste_matricula(self):
        return f"{self.coste_matricula}"