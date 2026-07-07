from models.academico.Clase_Seccion import Seccion

class Horario:
    def __init__(self, turno, hora_inicio, hora_fin, modalidad):
        self.turno = turno
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self._modalidad = modalidad

    def deteccion_colision(self, otro_horario):
        # Mejora: validación por rango de horas
        if self.turno == otro_horario.turno: #Verifica si los turnos son iguales
            #Verifica que las horas no se sobreponga entre si
            if self.hora_inicio < otro_horario.hora_fin and self.hora_fin > otro_horario.hora_inicio:
                return True
        return False

    def resumen_de_seccion(self, Seccion: Seccion):
        if Seccion.docentes:
            docentes_nombres =Seccion.docentes
        else:
            print("Sin docentes asignado")
            docentes_nombres=None

        return {
            "Turno": self.turno,
            "Inicio": self.hora_inicio,
            "Fin": self.hora_fin,
            "Modalidad": self._modalidad,
            "Docente": docentes_nombres
        }