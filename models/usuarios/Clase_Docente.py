from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico

class Docente(UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, especialidad):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.especialidades = especialidad

    def ver_rendimiento(self):
        return "Mostrando rendimiento de los estudiantes en la sección" #aqui se implementará la lógica para mostrar el rendimiento de los estudiantes en la sección que el docente imparte

    def ver_perfil(self):
        print(f"NOMBRE : {self.nombres}")
        print(f"APELLIDOS : {self.apellidos}")
        print(f"CORREO : {self.correo}")
        print(f"ESPECIALIDAD : {self.especialidad}")

    def colocar_calificacion(self):
        pass #Llama al metodo registrarNotaEstudiante() que se encuentra en seccion, luego se le mostrarán todos los estudiantes que se encuentren en esa seccion, y podra seleccionar al estudiante al que desea colocar la calificacion

    #El metodo para asignar a una seccion lo posee el coordinador