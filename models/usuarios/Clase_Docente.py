from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico

class Docente(UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.secciones = []
        self.especialidades = []

        
    def colocar_calificacion(self):
        print("Calificando actividad...")

    def tomar_asistencia(self):
        return 

    def ver_horario(self):
        return [seccion.lista_horarios for seccion in self.secciones]

    def asignar_seccion(self, seccion):
        if seccion not in self.secciones:
            self.secciones.append(seccion)
            seccion.agregar_docente(self)