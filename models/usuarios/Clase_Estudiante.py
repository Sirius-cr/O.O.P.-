from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico


class Estudiante(UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, id_estudiante, nombre_periodo, estado_matricula, tipo_matricula, historial = None):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)

        self._id_estudiante = id_estudiante
        self.nombre_periodo = nombre_periodo
        self.estado_matricula = estado_matricula
        self._tipo_matricula = tipo_matricula

        # El historial se inyectará después, o se iniciará vacío pero preparado para recibir el periodo
        self.historial = None
        self.secciones_asociadas = []

    def asignar_historial(self, historial_objeto):
            #Inyección de dependencias para desacoplar el historial
            self.historial = historial_objeto

    def inscribir_seccion(self, seccion):
            # Corrección de nombre de variable (secciones_asociadas -> seccion) pa enterderle mejor
            if seccion not in self.secciones_asociadas:
                self.secciones_asociadas.append(seccion)
                seccion.actualizar_estudiantes_inscritos(self)

    @property
    def esta_aprobado(self):
        if self.historial:
            return self.historial.verificar_aprobacion_nivelacion()
        return "Sin historial asignado"
    
    def ver_rendimiento(self):
        return self.historial.obtener_peor_nota() #este metodo se definirá en la clase HistorialAcademico para obtener la peor nota del estudiante en los parciales

    def ver_perfil(self):
        perfil = {
            "Cédula": self.cedula,
            "Nombre Completo": self.obtener_nombre_completo(),
            "Correo": self._correo,
            "Estado de Matrícula": self.estado_matricula,
            "Tipo de Matrícula": self.tipo_matricula
        }
        return perfil

    # --- REFACTORIZACIÓN SRP ---
    def ver_perfil(self):
        #Devuelve los datos estructurados en lugar de imprimirlos
        return {
            "rol": "Estudiante",
            "id_estudiante": self._id_estudiante,
            "cedula": self.cedula, # Usando el property de la clase padre
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "correo": self._correo
        }

    def solicitar_retiro(self):
        # Aquí se conectará con el Gestor de Reportes/Solicitudes de la Secretaria
        return True

    def solicitar_certificado(self):
        return True

    def obtener_historial_academico(self):
        return self.historial

    def solicitar_retiro(self):
        return True