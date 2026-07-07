from models.academico.Clase_Seccion import Seccion
class Horario:
    def __init__(self, turno, hora_inicio, hora_fin, modalidad, dias=None):
        self.turno = turno
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self._modalidad = modalidad
        self.dias = dias if dias is not None else ["Lunes", "Miércoles", "Viernes"]
    
    
    def deteccion_colision(self, otro_horario):
        def a_minutos(hora_str):
            try:
                h, m = map(int, hora_str.split(':'))
                return h * 60 + m
            except:
                return 0

        inicio1 = a_minutos(self.hora_inicio)
        fin1 = a_minutos(self.hora_fin)
        inicio2 = a_minutos(otro_horario.hora_inicio)
        fin2 = a_minutos(otro_horario.hora_fin)

        dias_en_comun = set(self.dias).intersection(set(otro_horario.dias))
        
        if dias_en_comun:
            if max(inicio1, inicio2) < min(fin1, fin2):
                return True
        return False

    def resumen_de_seccion(self, Seccion: Seccion):
        docentes_nombres = ", ".join(d.obtener_nombre_completo() for d in Seccion.docentes) if Seccion.docentes else "Sin docente asignado"
        return {
            "Turno de clase": self.turno,
            "Inicializacion": self.hora_inicio,
            "Terminacion": self.hora_fin,
            "Modalidad": self._modalidad,
            "Docente": docentes_nombres
        }

    