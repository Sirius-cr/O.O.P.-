# Importaciones reales de tu estructura de proyecto
from models.enums.Estado_Periodo import EstadoPeriodo
from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria, EstadoDeAprobacionNivelacion
from models.academico.Clase_Materia import Materia
from models.academico.Clase_Periodo import Periodo  # Tu clase periodo original
from models.usuarios.Clase_Estudiante import Estudiante

if __name__ == "__main__":
    print("=== INICIANDO PRUEBA DEL PATRÓN OBSERVER CON TU CLASE PERIODO ===\n")

    # 1. Creamos el Periodo Académico usando tu constructor real (Inicia en PLANIFICACIÓN)
    periodo_actual = Periodo(nombre_periodo="Nivelación Intensiva 2026", fecha_inicio="2026-06-01", fecha_final="2026-10-15")
    print(f"Periodo creado: {periodo_actual.nombre_periodo} | Estado inicial: {periodo_actual.estado_periodo}\n")

    # 2. Creamos asignaturas simuladas
    materia_poo = Materia(id_materia="POO-01", nombre_materia="Programación Orientada a Objetos")
    materia_calculo = Materia(id_materia="CAL-02", nombre_materia="Cálculo Diferencial")

    # 3. Inicializamos el Estudiante completo (quien a su vez creará su Historial Académico y se registrará como observador)
    estudiante = Estudiante(
        cedula="131555", 
        nombres="Julean", 
        apellidos="Pérez", 
        correo="julean@univ.com", 
        contrasenia="1234", 
        id_estudiante="HIST-JULEAN", 
        nombre_periodo="Nivelación Intensiva 2026", 
        tipo_matricula="Ordinaria"
    )
    historial = estudiante.historial

    # 4. PASO DE MATRÍCULA: El sistema registra las materias asociándoles el periodo correspondiente
    print("--- Proceso de Matrícula (El sistema genera los registros vacíos) ---")
    nota_poo = historial.crear_nota_materia(materia=materia_poo, periodo=periodo_actual, asistencia=85)
    nota_calculo = historial.crear_nota_materia(materia=materia_calculo, periodo=periodo_actual, asistencia=90)

    # 5. El periodo avanza en su ciclo de vida natural
    print("--- Transición del Periodo Académico ---")
    periodo_actual.iniciar_periodo()  # Cambia a EN CURSO

    # 6. El docente sube notas del Primer Parcial a través del objeto nota de la Sección
    print("\n--- Docentes asientan calificaciones del Parcial 1 ---")
    nota_poo.parcial1 = 8.0       # Llama al setter e invoca al Observer automáticamente
    nota_calculo.parcial1 = 5.5   # Llama al setter e invoca al Observer automáticamente

    # Verificamos que todo siga pendiente porque las actas no han cerrado (Periodo sigue EN CURSO)
    print(f"¿Estado Nivelación antes del cierre?: {historial.estado_nivelacion_actual.value}")
    print("(Correcto: Permanece 'Pendiente' porque el periodo no está Finalizado)\n")

    # 7. El periodo llega a su fin
    print("--- Cierre definitivo del Periodo Académico ---")
    periodo_actual.finalizar_periodo()  # Cambia a FINALIZADO

    # 8. Los docentes suben las notas del Parcial 2 (Ahora las propiedades de aprobación reaccionarán)
    print("\n--- Docentes asientan calificaciones del Parcial 2 (Con periodo FINALIZADO) ---")
    print("Modificando POO...")
    nota_poo.parcial2 = 9.0       # Promedio POO: 8.5 -> Aprobado

    print("Modificando Cálculo...")
    nota_calculo.parcial2 = 8.5   # Promedio Cálculo: 7.0 -> Aprobado

    print("=== FIN DE LA EVALUACIÓN DE REGLAS DE NEGOCIO ===")
    print(f"Estado Final de la Nivelación: {historial.estado_nivelacion_actual.name}")