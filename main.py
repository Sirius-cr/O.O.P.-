"""En este archivo de python tendremos un main que correra todo el backend
por el momento no hay nada xd -joseph"""
# main.py

# 1. Importaciones de tus modelos según la estructura del proyecto
from models.usuarios.Clase_Estudiante import Estudiante
from models.Clase_Materia import Materia
from models.Clase_NotaMateria import NotaMateria
from models.Clase_HistorialAcademico import HistorialAcademico

# Importamos los Enums para poder imprimir descripciones amigables en la terminal
from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria, EstadoDeAprobacionNivelacion

if __name__ == "__main__":
    print("--- 🎓 INICIANDO SIMULACIÓN DEL SISTEMA ACADÉMICO ---\n")

    # =========================================================================
    # PASO 1: Creación de Materias Globales de la Universidad
    # =========================================================================
    # Instanciamos los objetos Materia base
    materia_prog = Materia(id_materia="MAT-01", nombre_materia="Programación", nota_minima=7.0, asistencia_minima=70)
    materia_mate = Materia(id_materia="MAT-02", nombre_materia="Matemáticas", nota_minima=7.0, asistencia_minima=70)
    print(f"Materias disponibles registradas: '{materia_prog.nombre_materia}' y '{materia_mate.nombre_materia}'")


    # =========================================================================
    # PASO 2: Creación del Estudiante (Atributos nombres y apellidos públicos)
    # =========================================================================
    alumno = Estudiante(
        cedula="131555", 
        nombres="Julean", 
        apellidos="Pérez", 
        correo="julean@univ.com", 
        contrasenia="1234", 
        idEstudiante="EST-99", 
        nombrePeriodo="Nivelación 2026", 
        estadoMatricula="Matriculado", 
        tipoMatricula="Ordinaria"
    )
    # Al ser públicos nombres y apellidos, ya no arrojará AttributeError
    print(f"Estudiante ingresado al sistema: {alumno.nombres} {alumno.apellidos}")


    # =========================================================================
    # PASO 3: Asignación de Notas vinculadas a las Materias (Agregación)
    # =========================================================================
    # Creamos las NotaMateria inyectándoles su respectivo objeto Materia
    nota_prog = NotaMateria(materia=materia_prog)
    nota_mate = NotaMateria(materia=materia_mate)

    # Añadimos una propiedad dinámica en ejecución para emular el cierre del Coordinador
    nota_prog.periodo_cerrado = False
    nota_mate.periodo_cerrado = False

    # Guardamos los contenedores en el historial de Julean
    alumno.historial.agregarNotaMateria(nota_prog)
    alumno.historial.agregarNotaMateria(nota_mate)


    # =========================================================================
    # ESCENARIO 1: El Periodo Académico Sigue Abierto
    # =========================================================================
    print("\n--- ⏳ ESCENARIO 1: Notas en cero y periodo abierto por el Coordinador ---")
    
    # Modificamos tu método estaAprobado de NotaMateria temporalmente para esta simulación:
    def estaAprobado_con_coordinador(self_nota):
        if not getattr(self_nota, 'periodo_cerrado', False):
            return EstadoDeAprobacionMateria.MATERIA_PENDIENTE
        
        # Tu lógica original usando .value para extraer los enteros del Enum
        if (self_nota.notaFinal >= EstadoDeAprobacionMateria.NOTA_MINIMA_APROBACION.value and 
                self_nota.asistencia >= EstadoDeAprobacionMateria.ASISTENCIA_MINIMA.value):
            return EstadoDeAprobacionMateria.MATERIA_APROBADA
        else:
            return EstadoDeAprobacionMateria.MATERIA_REPROBADA

    # Enlazamos dinámicamente el comportamiento para la prueba de consola
    NotaMateria.estaAprobado = property(estaAprobado_con_coordinador)

    print(f"Estado en {nota_prog.materia.nombre_materia}: {nota_prog.estaAprobado.value}")
    print(f"VERDICTO FINAL DE NIVELACIÓN: -> {alumno.estaAprobado.value} <-")


    # =========================================================================
    # ESCENARIO 2: Profesor sube notas pero reprueba por asistencia
    # =========================================================================
    print("\n--- ❌ ESCENARIO 2: Profesor sube notas, Coordinador cierra ciclo (Falta de asistencia) ---")
    # Datos de Programación (Buen promedio, mala asistencia)
    nota_prog.parcial1 = 8.5
    nota_prog.parcial2 = 9.0
    nota_prog.asistencia = 55  # Por debajo del mínimo (70)
    nota_prog.periodo_cerrado = True

    # Datos de Matemáticas (Aprueba todo)
    nota_mate.parcial1 = 7.5
    nota_mate.parcial2 = 8.0
    nota_mate.asistencia = 95
    nota_mate.periodo_cerrado = True

    print(f"Promedio General calculado en Historial: {alumno.historial.promedioGeneral:.2f}")
    print(f"Estado en {nota_prog.materia.nombre_materia}: {nota_prog.estaAprobado.value} (Asistencia: {nota_prog.asistencia}%)")
    print(f"Estado en {nota_mate.materia.nombre_materia}: {nota_mate.estaAprobado.value}")
    print(f"VERDICTO FINAL DE NIVELACIÓN: -> {alumno.estaAprobado.value} <-")


    # =========================================================================
    # ESCENARIO 3: Alumno justifica asistencias y aprueba la Nivelación
    # =========================================================================
    print("\n--- 🏆 ESCENARIO 3: Estudiante justifica faltas y el sistema actualiza ---")
    # Modificamos la asistencia de la materia que estaba reprobada
    nota_prog.asistencia = 85  # Supera el mínimo requerido

    print(f"Nuevo estado en {nota_prog.materia.nombre_materia}: {nota_prog.estaAprobado.value}")
    print(f"VERDICTO FINAL DE NIVELACIÓN: -> {alumno.estaAprobado.value} <-")