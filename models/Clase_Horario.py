from Clase_Seccion import Seccion
class Horario:
    def __init__(self, turno, hora_inicio, hora_fin, modalidad):
        self.turno = turno
        self.hora_inicio =hora_inicio
        self.hora_fin=hora_fin
        self._modalidad=modalidad
    
    
    def Detenccion_Colision(self, otro_horario):
        if self.turno == otro_horario.turno:
            return True #"Error. El horario se choca con otra seccion"
        return False

    def resumen_de_Seccion(self,Seccion:Seccion):
        return {
            "Turno de clase":self.turno,
            "Inicializacion":self.hora_inicio,
            "Terminacion" : self.hora_fin,
            "Modalidad":self._modalidad,
            "Docente":self.docente_asignado
        }
    