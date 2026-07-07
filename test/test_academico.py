import sys
import os
# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# script_pruebas.py
from models.academico.Clase_AulaVirtual import AulaVirtual
from models.academico.Clase_Seccion import Seccion
from models.academico.Clase_Horario import Horario
from models.academico.Clase_MallaCurricular import MallaCurricular
from models.academico.Clase_Materia import Materia
from models.institucion.Clase_Carrera import Carrera

# 1. Instanciación de objetos para el test
carrera = Carrera("C01", "Ingeniería en Software", 50)
malla = carrera.crear_malla_curricular("M01", "Tecnología")
materia = Materia("MAT1", "Programación II")
malla.agregar_materias(materia)
seccion = materia.crear_seccion("S1", 30)
aula = AulaVirtual(20, "https://zoom.us/j/123", "Zoom")
horario = Horario("Matutino", "08:00", "10:00", "Presencial")

# Asignaciones necesarias
seccion.asignar_aula_virtual(aula)
seccion.agregar_horario(horario)

if __name__ == "__main__":
    while True:
        print("\n--- MENÚ DE PRUEBA DEL SISTEMA ---")
        print("1. Probar Carrera y Malla")
        print("2. Probar Materia y Seccion")
        print("3. Probar Aula Virtual (Ingresos)")
        print("4. Probar Horario y Colisiones")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                print(f"Carrera: {carrera.nombre_carrera}")
                print(f"Materias en Malla: {malla.listar_materias()}")
            
            case "2":
                print(f"Secciones en {materia.nombre_materia}: {seccion.id_seccion}")
                print(f"Resumen sección: {seccion.obtener_resumen()}")
                
            case "3":
                aula.registrar_ingreso("Juan Perez", seccion)
                print(f"Estado Aula: {aula.estado_aula(seccion)}")
                print(aula.finalizar_sesion_virtual(seccion, materia, 60))
                
            case "4":
                otro_horario = Horario("Matutino", "09:00", "11:00", "Presencial")
                colision = horario.deteccion_colision(otro_horario)
                print(f"¿Hay colisión de horarios?: {colision}")
                
            case "5":
                break
            case _:
                print("Opción no válida")

#Otro Prueba

# 1. Poblar el sistema con datos complejos
carrera = Carrera("C01", "Ingeniería en Software", 100)
malla = carrera.crear_malla_curricular("M01", "Programación Avanzada")

# Crear materias
mat1 = Materia("MAT1", "POO")
mat2 = Materia("MAT2", "Estructuras de Datos")
malla.agregar_materias(mat1)
malla.agregar_materias(mat2)

# Crear secciones con datos
sec1 = mat1.crear_seccion("S1-POO", 30)
sec1.agregar_docente("Ing. Ana Perez")
sec1.agregar_docente("Dr. Juan Silva")
sec1.actualizar_estudiantes_inscritos("Estudiante A")
sec1.actualizar_estudiantes_inscritos("Estudiante B")

# Crear aula y horarios
aula = AulaVirtual(20, "https://zoom.us/virtual", "Zoom Premium")
sec1.asignar_aula_virtual(aula)
sec1.agregar_horario(Horario("Matutino", "07:00", "09:00", "Presencial"))

if __name__ == "__main__":
    while True:
        print("\n--- TEST INTEGRAL: SISTEMA ACADÉMICO ---")
        print("1. [Reporte] Mostrar toda la estructura")
        print("2. [Gestión] Ver resumen de Secciones y Docentes")
        print("3. [Aula] Simular ingresos y cupos")
        print("4. [Horarios] Verificar colisiones reales")
        print("5. [Notas] Registrar nota y listar")
        print("6. [Salir]")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                carrera.mostrar_datos_carrera("PDF")
                print(f"Malla: {malla.codigo_malla} | Total materias: {malla.total_materias()}")
                
            case "2":
                print(f"Detalle {sec1.id_seccion}:")
                print(f"Docentes: {sec1.docentes}")
                print(f"Resumen: {sec1.obtener_resumen()}")
                
            case "3":
                print(f"Cupos totales: {sec1.calcular_limite_optimo()}")
                print(f"¿Inscritos pueden entrar?: {sec1.verificar_cupos_disponibles()}")
                print(f"Ingreso de alumno: {aula.registrar_ingreso('Estudiante A', sec1)}")
                
            case "4":
                h_base = sec1.lista_horarios[0]
                h_conflicto = Horario("Matutino", "08:00", "10:00", "Presencial")
                print(f"Base: {h_base.hora_inicio}-{h_base.hora_fin}")
                print(f"Conflicto: {h_conflicto.hora_inicio}-{h_conflicto.hora_fin}")
                print(f"¿Colisión?: {h_base.deteccion_colision(h_conflicto)}")
                
            case "5":
                sec1.registrar_nota_estudiante("Estudiante A", 9.5)
                print(f"Notas registradas: {sec1.registro_notas}")
                
            case "6":
                break
            case _:
                print("Opción inválida.")

#Prueba de la visualizacion de la lista 
# 1. Creación de componentes
    seccion = Seccion("S202", 40)
    horario1 = Horario("Matutino", "07:00", "09:00", "Presencial")
    aula = AulaVirtual(40, "https://meet.google.com/abc", "Google Meet")

    print("\n--- INICIO: ESTADO VACÍO ---")
    print(seccion.obtener_resumen())

    # 2. Alimentando el sistema a través de métodos
    print("\n--- POBLANDO DATOS ---")
    seccion.agregar_docente("Prof. Goku")
    seccion.agregar_docente("Prof. Vegetta 777")
    seccion.actualizar_estudiantes_inscritos("L")
    seccion.actualizar_estudiantes_inscritos("Mario sanchez")
    seccion.agregar_horario(horario1)
    seccion.asignar_aula_virtual(aula)

    # 3. Visualización de listas mediante métodos
    print("\n--- ESTADO DESPUÉS DE LOS MÉTODOS ---")
    print(f"Docentes registrados: {seccion.docentes}")
    print(f"Estudiantes inscritos: {seccion.estudiantes_inscritos}")
    print(f"Horarios registrados: {len(seccion.lista_horarios)}")
    print(f"Aula asignada: {seccion.aula_virtual}")

    # 4. Verificación de lógica calculada
    print("\n--- VALIDACIÓN FINAL ---")
    print(f"¿Existen cupos?: {seccion.verificar_cupos_disponibles()}")
    print(f"Resumen consolidado:\n{seccion.obtener_resumen()}")