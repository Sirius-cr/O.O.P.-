import sys
import os

# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.usuarios.Clase_Estudiante import Estudiante
from models.usuarios.Clase_Docente import Docente
from models.academico.Clase_Materia import Materia
from models.academico.Clase_Seccion import Seccion
from models.academico.Clase_AulaVirtual import AulaVirtual
from models.gestion.Clase_NotaMateria import NotaMateria
from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria
from models.institucion.Clase_Universidad import Universidad
from models.institucion.Clase_Sede import Sede
from models.institucion.Clase_Facultad import Facultad
from models.institucion.Clase_Carrera import Carrera

def limpiar_pantalla():
    # Limpia la consola en Windows o Unix
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_tecla():
    input("\nPresione Enter para continuar...")

def probar_usuarios():
    limpiar_pantalla()
    print("==================================================")
    print("         PRUEBA INTERACTIVA: MÓDULO USUARIOS      ")
    print("==================================================")
    
    print("\n--- Paso 1: Crear un Estudiante ---")
    cedula = input("Cédula: ").strip() or "1312345678"
    nombres = input("Nombres: ").strip() or "Juan"
    apellidos = input("Apellidos: ").strip() or "Pérez"
    correo = input("Correo: ").strip() or "juan.perez@live.uleam.edu.ec"
    contrasenia = input("Contraseña inicial: ").strip() or "clave123"
    id_est = input("ID Estudiante: ").strip() or "EST-01"
    periodo = input("Periodo Académico: ").strip() or "Nivelación 2026"
    
    estudiante = Estudiante(
        cedula=cedula,
        nombres=nombres,
        apellidos=apellidos,
        correo=correo,
        contrasenia=contrasenia,
        id_estudiante=id_est,
        nombre_periodo=periodo,
        estado_matricula="Matriculado",
        tipo_matricula="Ordinaria"
    )
    print(f"\n[OK] Estudiante creado: {estudiante.obtener_nombre_completo()}")
    
    print("\n--- Paso 2: Probar cambio de contraseña ---")
    contrasenia_act = input(f"Ingrese contraseña actual (para verificar): ").strip()
    nueva_contrasenia = input("Ingrese nueva contraseña (mínimo 8 caracteres): ").strip()
    
    resultado_pass = estudiante.cambiar_contrasenia(contrasenia_act, nueva_contrasenia)
    if resultado_pass:
        print("[ÉXITO] Contraseña modificada correctamente.")
    else:
        print("[FALLO] No se pudo cambiar la contraseña. Verifique que la contraseña actual sea correcta y que la nueva tenga 8 o más caracteres.")
        
    print("\n--- Paso 3: Probar actualización de datos de contacto ---")
    nuevo_correo = input("Ingrese nuevo correo de contacto: ").strip()
    nuevo_telf = input("Ingrese nuevo teléfono: ").strip()
    
    resultado_contacto = estudiante.actualizar_datos_contacto(nuevo_correo, nuevo_telf)
    if resultado_contacto:
        print(f"[ÉXITO] Datos de contacto actualizados. Nuevo correo: {estudiante._correo}")
    else:
        print("[FALLO] Formato de correo inválido (debe contener '@').")

def probar_academico():
    limpiar_pantalla()
    print("==================================================")
    print("        PRUEBA INTERACTIVA: MÓDULO ACADÉMICO      ")
    print("==================================================")
    
    print("\n--- Paso 1: Crear Materia y Sección ---")
    nombre_mat = input("Nombre de la Materia: ").strip() or "Programación II"
    cap_seccion_str = input("Capacidad de la Sección: ").strip() or "30"
    
    try:
        cap_seccion = int(cap_seccion_str)
    except ValueError:
        print("Entrada inválida. Se usará capacidad de 30.")
        cap_seccion = 30
        
    materia = Materia("MAT-PROG", nombre_mat)
    seccion = Seccion("SEC-01", cap_seccion, materia=materia)
    print(f"\n[OK] Sección '{seccion.id_seccion}' creada con capacidad para {seccion.capacidad_estudiantil} estudiantes.")
    
    print("\n--- Paso 2: Asignar Aula Virtual (Opcional) ---")
    asignar_aula = input("¿Desea asignar un Aula Virtual? (s/n): ").strip().lower()
    if asignar_aula == 's':
        cap_aula_str = input("Capacidad máxima del Aula Virtual: ").strip() or "20"
        try:
            cap_aula = int(cap_aula_str)
        except ValueError:
            cap_aula = 20
        aula = AulaVirtual(capacidad_maxima=cap_aula, enlace_plataforma="http://teams.uleam.edu.ec", tipo_plataforma="Teams")
        seccion.asignar_aula_virtual(aula)
        print(f"[OK] Aula Virtual asignada con capacidad de {cap_aula}.")
    
    limite = seccion.calcular_limite_optimo()
    print(f"\n[INFO] Límite optimizado calculado de la sección: {limite} estudiantes.")
    
    print("\n--- Paso 3: Simular inscripción de estudiantes ---")
    num_est_str = input("¿Cuántos estudiantes desea intentar inscribir?: ").strip() or "5"
    try:
        num_est = int(num_est_str)
    except ValueError:
        num_est = 5
        
    print(f"\nInscribiendo {num_est} estudiantes...")
    for i in range(1, num_est + 1):
        temp_est = Estudiante(
            cedula=f"1312345{i:03d}",
            nombres=f"Estudiante{i}",
            apellidos="Prueba",
            correo=f"est{i}@uleam.edu.ec",
            contrasenia="pass123",
            id_estudiante=f"EST-{i:03d}",
            nombre_periodo="2026",
            estado_matricula="Matriculado",
            tipo_matricula="Ordinaria"
        )
        # El estudiante se inscribe en la sección
        estudiante_inscribir = temp_est.inscribir_seccion(seccion)
        # Obtenemos si está en la lista de inscritos
        if temp_est in seccion.estudiantes_inscritos:
            print(f"  -> [INSCRITO] Estudiante{i} agregado con éxito.")
        else:
            print(f"  -> [DENEGADO] Estudiante{i} rebotó. Razón: No existen cupos disponibles.")

    print(f"\nEstado final de la sección:")
    print(f"  - Total inscritos: {len(seccion.estudiantes_inscritos)}")
    print(f"  - Sección disponible para más cupos: {seccion.disponibilidad}")

def probar_gestion():
    limpiar_pantalla()
    print("==================================================")
    print("         PRUEBA INTERACTIVA: MÓDULO GESTIÓN       ")
    print("==================================================")
    
    print("\n--- Paso 1: Ingreso de Calificaciones ---")
    materia_nombre = input("Nombre de la materia a evaluar: ").strip() or "Cálculo Diferencial"
    
    try:
        parcial1 = float(input("Nota del Parcial 1 (0.0 - 10.0): ").strip() or "0.0")
        parcial2 = float(input("Nota del Parcial 2 (0.0 - 10.0): ").strip() or "0.0")
        asistencia = int(input("Porcentaje de asistencia (0 - 100): ").strip() or "0")
    except ValueError:
        print("[ERROR] Entrada numérica inválida. Se usarán valores predeterminados (0).")
        parcial1, parcial2, asistencia = 0.0, 0.0, 0
        
    materia = Materia("MAT-CALC", materia_nombre)
    nota_materia = NotaMateria(materia=materia, parcial1=parcial1, parcial2=parcial2, asistencia=asistencia)
    
    print("\n--- Paso 2: Resultados calculados ---")
    print(f"Materia:      {nota_materia.materia.nombre_materia}")
    print(f"Nota Parcial 1: {nota_materia.parcial1}")
    print(f"Nota Parcial 2: {nota_materia.parcial2}")
    print(f"Nota Final:     {nota_materia.nota_final:.2f}")
    print(f"Asistencia:     {nota_materia.asistencia}%")
    
    print("\n--- Paso 3: Decisión del Sistema ---")
    estado = nota_materia.esta_aprobado
    print(f"VERDICTO: -> {estado.value} <-")
    if estado == EstadoDeAprobacionMateria.MATERIA_APROBADA:
        print("¡Felicidades! Cumple con la nota minima (>= 7.0) y la asistencia (>= 70%).")
    else:
        print("Reprobado. No cumple con la nota minima o asistencia requerida.")

def probar_institucion():
    limpiar_pantalla()
    print("==================================================")
    print("       PRUEBA INTERACTIVA: MÓDULO INSTITUCIÓN     ")
    print("==================================================")
    
    print("\n--- Paso 1: Crear Universidad y Sede ---")
    nombre_uni = input("Nombre de la Universidad: ").strip() or "ULEAM"
    nombre_sede = input("Nombre de la Sede: ").strip() or "Sede Manta"
    ubicacion = input("Ubicación/Ciudad de la Sede: ").strip() or "Manta"
    direccion = input("Dirección física de la Sede: ").strip() or "Vía San Mateo"
    
    universidad = Universidad(nombre_uni, "U-01")
    sede = Sede(nombre_sede, ubicacion, direccion)
    universidad.agregar_sede(sede)
    print(f"\n[OK] Universidad '{universidad.nombre_uni}' registrada con sede '{sede.nombre_sede}'.")
    
    print("\n--- Paso 2: Registrar Facultad ---")
    nombre_fac = input("Nombre de la Facultad: ").strip() or "Facultad de Ingeniería"
    try:
        salones = int(input("Número de salones: ").strip() or "10")
        labs = int(input("Número de laboratorios: ").strip() or "5")
    except ValueError:
        salones, labs = 10, 5
        
    facultad = Facultad(nombre_fac, salones, labs)
    msg_fac = sede.agregar_facultad(facultad)
    print(f"[OK] {msg_fac}")
    
    print("\n--- Paso 3: Vincular Carrera ---")
    id_carrera = input("Código único de la Carrera (Ej: SOFT): ").strip().upper() or "SOFT"
    nombre_carrera = input("Nombre completo de la Carrera: ").strip() or "Ingeniería en Software"
    try:
        cap_carrera = int(input("Capacidad máxima de estudiantes en la carrera: ").strip() or "100")
    except ValueError:
        cap_carrera = 100
        
    carrera = Carrera(id_carrera, nombre_carrera, cap_carrera)
    msg_carrera = facultad.importar_carrera(carrera)
    print(f"[OK] {msg_carrera}")
    
    print("\n--- Paso 4: Reporte final de la Carrera ---")
    formato = input("Formato del reporte (Ej: PDF / TXT / EXCEL): ").strip().upper() or "PDF"
    reporte = carrera.mostrar_datos_carrera(formato)
    
    # Imprimimos el reporte generado
    print(reporte.imprimir_reporte())

def main_menu():
    while True:
        limpiar_pantalla()
        print("==================================================")
        print("     SISTEMA ACADÉMICO - INTERFAZ DE PRUEBAS      ")
        print("==================================================")
        print("Seleccione el módulo que desea probar interactuando:")
        print("1. Probar Módulo Usuarios (Estudiante, Docente, contraseñas)")
        print("2. Probar Módulo Académico (Sección, AulaVirtual, cupos)")
        print("3. Probar Módulo Gestión (Notas, promedio, aprobación)")
        print("4. Probar Módulo Institución (Universidad, Sede, Facultad, Carrera)")
        print("5. Salir")
        print("==================================================")
        
        opcion = input("Ingrese una opción (1-5): ").strip()
        
        if opcion == '1':
            probar_usuarios()
            esperar_tecla()
        elif opcion == '2':
            probar_academico()
            esperar_tecla()
        elif opcion == '3':
            probar_gestion()
            esperar_tecla()
        elif opcion == '4':
            probar_institucion()
            esperar_tecla()
        elif opcion == '5':
            print("\nSaliendo del sistema de pruebas. ¡Hasta luego!\n")
            break
        else:
            print("\n[ERROR] Opción no válida. Intente de nuevo.")
            esperar_tecla()

if __name__ == '__main__':
    main_menu()
