from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico
from models.patrones_diseno.strategy.ReporteStrategy import Reporte

class Docente(UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, especialidad):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.especialidad = especialidad
        self.secciones = []

    def ver_rendimiento(self):
        todas_notas = []
        for sec in self.secciones:
            for est in sec.estudiantes_inscritos:
                nota_obj = next((n for n in est.historial.lista_nota_materia if n.materia.id_materia == sec.materia.id_materia), None)
                if nota_obj:
                    todas_notas.append(nota_obj.nota_final)
        return sum(todas_notas) / len(todas_notas) if todas_notas else 0.0

    def ver_perfil(self):
        print(f"NOMBRE : {self.nombres}")
        print(f"APELLIDOS : {self.apellidos}")
        print(f"CORREO : {self.correo}")
        print(f"ESPECIALIDAD : {self.especialidad}")

    def colocar_calificacion(self, nota, parcial, valor):
        if parcial == 1:
            nota.parcial1 = valor
        elif parcial == 2:
            nota.parcial2 = valor
        nota.ultimo_modificador = self.obtener_nombre_completo()
        return True

    def tomar_asistencia(self, nota, valor):
        nota.asistencia = valor
        nota.ultimo_modificador = self.obtener_nombre_completo()
        return True

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

    def ver_horario(self):
        horarios_list = []
        for sec in self.secciones:
            for h in sec.lista_horarios:
                horarios_list.append({
                    "materia": sec.materia.nombre_materia if sec.materia else "",
                    "seccion": sec.id_seccion,
                    "modalidad": h._modalidad,
                    "dias": h.dias,
                    "turno": h.turno,
                    "inicio": h.hora_inicio,
                    "fin": h.hora_fin,
                    "aula": sec.aula_virtual._enlace_plataforma if sec.aula_virtual else None
                })
        return horarios_list

            