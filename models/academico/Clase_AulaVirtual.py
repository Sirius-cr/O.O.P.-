import csv
from datetime import datetime


class AulaVirtual:
    def __init__(self, capacidad_maxima, enlace_plataforma, tipo_plataforma):
        self.capacidad_maxima = capacidad_maxima
        self._enlace_plataforma = enlace_plataforma
        self._tipo_plataforma = tipo_plataforma

        # Lista de estudiantes que realmente ingresaron a la sesión virtual
        self.estudiantes_conectados = []

    # =========================================================
    # OBTENER INFORMACIÓN DE ACCESO
    # =========================================================
    def obtener_acceso(self):
        """
        Permite consultar el tipo de plataforma y el enlace.
        """

        return {
            "tipo_plataforma": self._tipo_plataforma,
            "enlace": self._enlace_plataforma,
            "estado": "ACTIVO"
        }

    # =========================================================
    # VALIDAR ACCESO DE ESTUDIANTE
    # =========================================================
    def validar_acceso_estudiante(self, estudiante, seccion):
        """
        Verifica si un estudiante puede ingresar al aula virtual
        según la capacidad máxima definida.
        """

        return len(self.estudiantes_conectados) < self.capacidad_maxima

    # =========================================================
    # REGISTRAR INGRESO A SESIÓN VIRTUAL
    # =========================================================
    def registrar_ingreso(self, estudiante, seccion):
        """
        Registra el ingreso REAL de un estudiante al aula virtual.

        """

        if len(self.estudiantes_conectados) < self.capacidad_maxima:

            if estudiante not in self.estudiantes_conectados:
                self.estudiantes_conectados.append(estudiante)

            return f"{estudiante} ha ingresado al aula virtual"

        return "Acceso denegado: aula llena"

    # =========================================================
    # ESTADO DEL AULA VIRTUAL
    # =========================================================
    def estado_aula(self, seccion):
        """
        Retorna información del uso actual del aula virtual.

        """

        ocupados = len(self.estudiantes_conectados)

        return {
            "capacidad_maxima": self.capacidad_maxima,
            "estudiantes_conectados": ocupados,
            "disponibles": self.capacidad_maxima - ocupados,
            "porcentaje_uso": round((ocupados / self.capacidad_maxima) * 100, 2)
            if self.capacidad_maxima > 0 else 0
        }

    # =========================================================
    # INICIAR SESIÓN VIRTUAL
    # =========================================================
    def iniciar_sesion_virtual(self, seccion, materia):
        """
        Retorna información básica de la sesión.
        """

        return {
            "estado": "ACTIVA",
            "materia": materia.nombre_materia if materia else "Sin materia",
            "seccion": seccion.id_seccion,
            "capacidad_maxima": self.capacidad_maxima,
            "hora_inicio": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    # =========================================================
    # FINALIZAR SESIÓN VIRTUAL (REPORTE COMPLETO)
    # =========================================================
    def finalizar_sesion_virtual(self, seccion, materia, duracion_minutos=0):
        """
        Genera un reporte completo de la sesión virtual finalizada.
        """

        ocupados = len(self.estudiantes_conectados)

        return {
            "materia": materia.nombre_materia if materia else "Sin materia",
            "seccion": seccion.id_seccion,
            "estudiantes_conectados": ocupados,
            "capacidad_maxima": self.capacidad_maxima,
            "porcentaje_uso": round((ocupados / self.capacidad_maxima) * 100, 2)
            if self.capacidad_maxima > 0 else 0,
            "duracion_minutos": duracion_minutos,
            "hora_finalizacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "estado": "FINALIZADA"
        }

    # =========================================================
    #  EXPORTAR ESTUDIANTES A CSV (SOLO CONECTADOS)
    # =========================================================
    def exportar_lista_estudiantes_excel(self, seccion, nombre_archivo=None):
        """
        Exporta SOLO los estudiantes que ingresaron al aula virtual
        a un archivo CSV compatible con Excel.
        """

        if nombre_archivo is None:
            nombre_archivo = f"ingresos_aula_{seccion.id_seccion}.csv"

        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Encabezados
            writer.writerow([
                "Estudiante",
                "Seccion",
                "Materia",
                "Fecha Exportacion"
            ])

            # Solo estudiantes que realmente ingresaron
            for estudiante in self.estudiantes_conectados:
                writer.writerow([
                    estudiante,
                    seccion.id_seccion,
                    seccion.materia.nombre_materia if seccion.materia else "Sin materia",
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ])

        return f"Archivo generado correctamente: {nombre_archivo}"

    # =========================================================
    # GUARDAR HISTORIAL DE SESIÓN
    # =========================================================
    def guardar_reporte_sesion(self, seccion, materia, duracion_minutos=0):
        """
        Guarda el historial de una sesión virtual en archivo CSV.

        Permite almacenar múltiples sesiones en el tiempo.
        """

        archivo = f"reporte_sesion_{seccion.id_seccion}.csv"

        ocupados = len(self.estudiantes_conectados)

        with open(archivo, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                materia.nombre_materia if materia else "Sin materia",
                seccion.id_seccion,
                ocupados,
                self.capacidad_maxima,
                duracion_minutos,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])

        return f"Reporte guardado en {archivo}"

    # =========================================================
    # CERRAR SESIÓN VIRTUAL
    # =========================================================
    def cerrar_sesion(self):
        """
        Limpia la lista de estudiantes conectados.

        Simula el cierre total del aula virtual.
        """

        self.estudiantes_conectados = []
        return "Sesión virtual cerrada correctamente"