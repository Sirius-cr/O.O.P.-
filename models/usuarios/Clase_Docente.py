from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico
from models.patrones_diseno.strategy.ReporteStrategy import Reporte

class Docente(UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.secciones = []
        self.especialidades = []

    def ver_rendimiento(self):
        return "Mostrando rendimiento de los estudiantes en la sección" #aqui se implementará la lógica para mostrar el rendimiento de los estudiantes en la sección que el docente imparte

    def ver_perfil(self):
        print(f"NOMBRE : {self.nombres}")
        print(f"APELLIDOS : {self.apellidos}")
        print(f"CORREO : {self.correo}")
        print(f"ESPECIALIDAD : {self.especialidad}")

    def colocar_calificacion(self):
        pass #Llama al metodo registrarNotaEstudiante() que se encuentra en seccion, luego se le mostrarán todos los estudiantes que se encuentren en esa seccion, y podra seleccionar al estudiante al que desea colocar la calificacion

    def tomar_asistencia(self):
        return 

    def asignar_seccion(self, seccion):
        if seccion not in self.secciones:
            self.secciones.append(seccion)
            seccion.agregar_docente(self)

    def realizaReporte(self, tipo_de_reporte, formato_documento, contenido):
        return Reporte(
            tipo_de_reporte=tipo_de_reporte,
            formato_documento=formato_documento,
            emisor=self.obtener_nombre_completo(),
            contenido=contenido
        )

            