from models.academico.Clase_AulaVirtual import AulaVirtual
class Seccion:
    def __init__(self, id_seccion, capacidad_estudiantil, materia=None, coordinador=None):
        self.id_seccion = id_seccion
        self.capacidad_estudiantil = capacidad_estudiantil
        self.materia = materia
        self.coordinador = coordinador
        self.estudiantes_inscritos = []
        self.lista_horarios = []
        self.docentes = []
        self.entorno_asignado = None
        self.aula_virtual = None
        self.disponibilidad = True

    def agregar_horario(self, horario):
        if horario not in self.lista_horarios:
            self.lista_horarios.append(horario)

    def asignar_aula_virtual(self, aula_virtual):
        self.aula_virtual = aula_virtual
        self.entorno_asignado = aula_virtual
        return "Aula asignada"

    def calcular_limite_optimo(self):
        if self.entorno_asignado is None:
            return self.capacidad_estudiantil
        return min(self.capacidad_estudiantil, self.entorno_asignado.capacidad_maxima)

    def verificar_cupos_disponibles(self):
        return len(self.estudiantes_inscritos) < self.calcular_limite_optimo()

    def importar_lista_horario(self, lista_horario):
        self.lista_horarios = lista_horario
        return self.lista_horarios

    def agregar_docente(self, docente):
        if docente not in self.docentes:
            self.docentes.append(docente)
            if hasattr(docente, 'asignar_seccion'):
                docente.asignar_seccion(self)
        return "Docente asignado"

    def asignar_entorno(self, entorno):
        self.entorno_asignado = entorno
        return "Entorno asignado"

    def liberar_cupo(self, estudiante):
        if estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.remove(estudiante)
            self.disponibilidad = True
            return "Cupo liberado"
        return False

    def actualizar_estudiantes_inscritos(self,estudiante):
        if self.verificar_cupos_disponibles():
            if estudiante not in self.estudiantes_inscritos:
                self.estudiantes_inscritos.append(estudiante)

                if not self.verificar_cupos_disponibles():
                    self.disponibilidad = False

                return "Estudiante inscrito"
            return "Ya inscrito"
        return "Sin cupos"

    def crear_entorno_academico(self, entorno:AulaVirtual):
        self.entorno_asignado = entorno
        return True

    def registrar_nota_estudiante(self, estudiante, nota):
        if not hasattr(self, "registro_notas"):
            self.registro_notas = {}

        self.registro_notas[estudiante] = nota
        return "Nota registrada"

    def obtener_resumen(self):
        return {
            "seccion": self.id_seccion,
            "estudiantes": len(self.estudiantes_inscritos),
            "docentes": len(self.docentes),
            "cupos": self.calcular_limite_optimo()
        }