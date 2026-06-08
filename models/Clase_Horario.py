class Horario:
    def __init__(self, turno, hora_inicio, hora_fin, modalidad):
        self.turno = turno
        self.hora_inicio =hora_inicio
        self.hora_fin=hora_fin
        self.__modalidad=modalidad
    
    def ocultar_horario_lleno(self):
        pass