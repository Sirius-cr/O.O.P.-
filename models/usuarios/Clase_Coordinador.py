from models.usuarios.Clase_UsuarioAdministrativo import UsuarioAdministrativo
from models.academico.Clase_Periodo import Periodo
from models.patrones_diseno.strategy.ReporteStrategy import Reporte

class Coordinador(UsuarioAdministrativo):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, id_coordinador, fecha_asignacion_cargo):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.id_coordinador = id_coordinador
        self.fecha_asignacion_cargo = fecha_asignacion_cargo
        self.carrera = None
        self.secciones_coordinadas = []

    def asociar_carrera(self, carrera):
        if self.carrera != carrera:
            self.carrera = carrera
            carrera.asociar_coordinador(self)

    def coordinar_seccion(self, seccion):
        if seccion not in self.secciones_coordinadas:
            self.secciones_coordinadas.append(seccion)
            seccion.coordinador = self
        
    def abrir_periodo_matricula(self, periodo: Periodo):
        periodo.iniciar_periodo()
        return True

    def cerrar_periodo_matricula(self, periodo: Periodo):
        periodo.finalizar_periodo()
        return True

    def aprobar_retiro(self):
        #Se implementará una vez que tengamos la base de datos lista
        return True

    def asignar_docente_a_seccion(self):
        return True
        #Se terminará de programar despues de que seccion se realice correctamente con un builder

    def asignar_lista_estudiante(self):        
        #Se implementará una vez que tengamos la base de datos lista
        return True
        
    def ver_perfil(self):
        perfil = {
            "Cédula": self.cedula,
            "Nombre Completo": self.obtener_nombre_completo(),
            "Correo": self._correo,
            "ID Coordinador": self.id_coordinador,
            "Fecha de Asignación al Cargo": self.fecha_asignacion_cargo
        }
        return perfil

    
    def filtrar_docentes_por_especialidad(self, docentes, especialidad):
        docentes_filtrados = []

        for docente in docentes:
            if especialidad in docente.especialidades:
                docentes_filtrados.append(docente)

        return docentes_filtrados
    