from models.usuarios.Clase_UsuarioAdministrativo import UsuarioAdministrativo
from models.academico.Clase_Periodo import Periodo
from models.gestion.Clase_Reporte import Reporte

class Coordinador(UsuarioAdministrativo):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, id_coordinador, fecha_asignacion_cargo):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.id_coordinador = id_coordinador
        self.fecha_asignacion_cargo = fecha_asignacion_cargo
        self.carreras = []
        self.secciones_coordinadas = []

    def asociar_carrera(self, carrera):
        if carrera not in self.carreras:
            self.carreras.append(carrera)
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
        return True

# --- NUEVOS MÉTODOS DE FILTRADO Y ASIGNACIÓN ---

    def obtener_docentes_por_materia(self, materia, lista_total_docentes):
        """
        Filtra y devuelve solo los docentes que tienen la materia en sus especialidades.
        """
        docentes_aptos = [
            docente for docente in lista_total_docentes 
            if materia in docente.especialidades
        ]
        return docentes_aptos

    def asignar_docente_a_seccion(self, seccion, lista_total_docentes):
        """
        Muestra o selecciona automáticamente un docente apto para la materia de la sección.
        """
        # Asumiendo que 'seccion' conoce a qué 'materia' pertenece (ej. seccion.materia)
        materia_requerida = seccion.materia 
        
        docentes_disponibles = self.obtener_docentes_por_materia(materia_requerida, lista_total_docentes)
        
        if not docentes_disponibles:
            print(f"No hay docentes especializados en {materia_requerida.nombre}")
            return False
            
        # Aquí puedes integrar la lógica de tu Builder o interfaz visual.
        # Por ahora, como ejemplo, asignamos el primer docente apto disponible:
        docente_elegido = docentes_disponibles[0] 
        docente_elegido.asignar_seccion(seccion)
        return True