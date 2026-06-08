class Horario:
    def __init__(self, turno, hora_inicio, hora_fin, modalidad):
        self.turno = turno
        self.hora_inicio =hora_inicio
        self.hora_fin=hora_fin
        self.__modalidad=modalidad
    
    
    def Detenccion_Colision(self, otro_horario):
        if self.turno == otro_horario.turno:
            pass
        return False
