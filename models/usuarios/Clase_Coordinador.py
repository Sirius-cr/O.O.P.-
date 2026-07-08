from models.usuarios.Clase_UsuarioAdministrativo import UsuarioAdministrativo
from models.academico.Clase_Periodo import Periodo
from models.patrones_diseno.strategy.ReporteStrategy import Reporte

class Coordinador(UsuarioAdministrativo):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, id_coordinador, fecha_asignacion_cargo, carrera=None):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.id_coordinador = id_coordinador
        self.fecha_asignacion_cargo = fecha_asignacion_cargo
        self.carrera = None
        self.secciones_coordinadas = []
        if carrera is not None:
            self.asociar_carrera(carrera)

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

    def cerrar_periodo_matricula(self, periodo: Periodo, lista_estudiantes=None):
        periodo.finalizar_periodo()
        if lista_estudiantes:
            for est in lista_estudiantes:
                for sec in est.secciones_asociadas:
                    if sec.materia:
                        nota_obj = next((n for n in est.historial.lista_nota_materia if n.materia.id_materia == sec.materia.id_materia), None)
                        if not nota_obj:
                            est.historial.crear_nota_materia(
                                materia=sec.materia,
                                periodo=periodo,
                                parcial1=0.0,
                                parcial2=0.0,
                                asistencia=0
                            )
                for nota in est.historial.lista_nota_materia:
                    nota.periodo_cerrado = True
                est.historial.actualizar()
        return True

    def aprobar_retiro(self, estudiante, solicitud, accion):
        if accion == 'aprobar':
            solicitud['estado'] = 'Aprobado'
            if estudiante:
                estudiante.esta_activo = 0
                for sec in list(estudiante.secciones_asociadas):
                    sec.liberar_cupo(estudiante)
                    estudiante.secciones_asociadas.remove(sec)
            return True
        else:
            solicitud['estado'] = 'Rechazado'
            return False

    def asignar_docente_a_seccion(self, docente, seccion):
        if docente.especialidad.lower() != seccion.materia.nombre_materia.lower():
            raise ValueError(f"La especialidad del docente ({docente.especialidad}) no coincide con la materia ({seccion.materia.nombre_materia}).")
        seccion.asignar_docente(docente)
        return True

    def asignar_horario_a_seccion(self, seccion, nuevo_horario, todas_secciones):
        for otra_sec in todas_secciones:
            for horario in otra_sec.lista_horarios:
                if nuevo_horario.deteccion_colision(horario):
                    raise ValueError(f"El horario choca con la sección {otra_sec.id_seccion} ({otra_sec.materia.nombre_materia}) en el horario {horario.hora_inicio}-{horario.hora_fin} los días {', '.join(horario.dias)}.")
        seccion.agregar_horario(nuevo_horario)
        return True

