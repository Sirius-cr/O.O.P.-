import sys
import os

# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.academico.Clase_Materia import Materia
from models.academico.Clase_AulaVirtual import AulaVirtual
from models.patrones_diseno.builders.SeccionBuilder import SeccionBuilder

def main():
    print("==================================================")
    print("  CREACION INTERACTIVA DE SECCION CON BUILDER ")
    print("==================================================")
    print("Vamos a construir una Seccion paso a paso.\n")

    # Inicializamos el Builder
    builder = SeccionBuilder()

    # 1. ID de Sección (Campo Obligatorio)
    while True:
        id_seccion = input("1. Ingrese el ID de la Sección (ej. SEC-101): ").strip()
        if id_seccion:
            builder.con_id_seccion(id_seccion)
            break
        print("[ERROR] El ID de la sección no puede estar vacío.")

    # 2. Capacidad Estudiantil (Campo Obligatorio)
    while True:
        capacidad_str = input("2. Ingrese la capacidad estudiantil (ej. 30): ").strip()
        try:
            capacidad = int(capacidad_str)
            if capacidad > 0:
                builder.con_capacidad_estudiantil(capacidad)
                break
            print("[ERROR] La capacidad debe ser mayor que 0.")
        except ValueError:
            print("[ERROR] Por favor ingrese un número entero válido.")

    # 3. Materia (Campo Opcional)
    nombre_materia = input("3. Ingrese el nombre de la Materia (opcional, presione Enter para omitir): ").strip()
    if nombre_materia:
        # Creamos una Materia de prueba para asignarla
        materia = Materia(id_materia="MAT-TEMP", nombre_materia=nombre_materia)
        builder.con_materia(materia)
        print(f"   -> Materia '{nombre_materia}' agregada al Builder.")
    else:
        print("   -> Se omitió la asignación de materia.")

    # 4. Aula Virtual (Campo Opcional)
    aula_resp = input("4. ¿Desea asignar un Aula Virtual? (s/n): ").strip().lower()
    if aula_resp == 's':
        while True:
            cap_aula_str = input("   Ingrese la capacidad máxima del aula virtual (ej. 25): ").strip()
            try:
                cap_aula = int(cap_aula_str)
                if cap_aula > 0:
                    aula = AulaVirtual(capacidad_maxima=cap_aula, enlace_plataforma="http://virtual.uleam.edu.ec", tipo_plataforma="Teams")
                    builder.con_aula_virtual(aula)
                    print(f"   -> Aula Virtual (capacidad: {cap_aula}) agregada al Builder.")
                    break
                print("[ERROR] La capacidad debe ser mayor que 0.")
            except ValueError:
                print("[ERROR] Por favor ingrese un número entero válido.")
    else:
        print("   -> Se omitió la asignación de aula virtual.")

    # 5. Disponibilidad (Campo Opcional)
    disp_resp = input("5. ¿La sección está disponible para inscripciones? (s/n, defecto 's'): ").strip().lower()
    if disp_resp == 'n':
        builder.con_disponibilidad(False)
        print("   -> Disponibilidad establecida en False.")
    else:
        builder.con_disponibilidad(True)
        print("   -> Disponibilidad establecida en True.")

    print("\n--------------------------------------------------")
    print("Construyendo el objeto Sección con el Builder...")
    print("--------------------------------------------------")
    
    try:
        # Llamamos al método build() para construir la sección
        seccion_creada = builder.build()
        
        # Mostramos los detalles del objeto final creado
        print("\nSeccion construida exitosamente con SeccionBuilder!")
        print(f" - ID de Sección:          {seccion_creada.id_seccion}")
        print(f" - Capacidad Estudiantil:  {seccion_creada.capacidad_estudiantil}")
        print(f" - Materia Asignada:       {seccion_creada.materia.nombre_materia if seccion_creada.materia else 'Ninguna'}")
        print(f" - Aula Virtual Asignada:  {f'Sí (Capacidad: {seccion_creada.aula_virtual.capacidad_maxima})' if seccion_creada.aula_virtual else 'No'}")
        print(f" - Disponibilidad:         {seccion_creada.disponibilidad}")
        print(f" - Límite Óptimo Calculado: {seccion_creada.calcular_limite_optimo()}")
        print("==================================================")
        
    except Exception as e:
        print(f"Ocurrio un error al construir la seccion: {e}")

if __name__ == '__main__':
    main()
