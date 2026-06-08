"""
Aqui es una prueba de mi modulo, funciona para entrada por terminal.
Hay que programar la interfaz para fuera de la terminal cuando lanzen el web.
Si no se logra pues se corrige esto para que haga parte del main

"""
from models.Clase_Universidad import Universidad
from models.Clase_Sede import Sede
from models.Clase_Facultad import Facultad
from models.Clase_Carrera import Carrera

class ControladorConsola:
    def __init__(self):
        self.registro_universidades = {}

    def registrar_universidad(self):
        print("\n--- REGISTRAR UNIVERSIDAD ---")
        nombre = input("Nombre de la Universidad: ").strip()
        codigo = input("Codigo unico de busqueda (Ej: ULEAM): ").strip().upper()

        if not nombre or not codigo:
            print("Error: Todos los campos son obligatorios.")
            return

        if codigo in self.registro_universidades:
            print(f"Error: Ya existe una universidad con el codigo [{codigo}].")
            return

        self.registro_universidades[codigo] = Universidad(nombre, codigo)
        print(f"Universidad '{nombre}' registrada con exito bajo el codigo [{codigo}].")

    def registrar_sede(self):
        print("\n--- REGISTRAR SEDE EN UNIVERSIDAD ---")
        if not self.registro_universidades:
            print("Error: No hay universidades registradas en el sistema.")
            return

        codigo_uni = input("Ingrese el codigo de la universidad destino: ").strip().upper()
        universidad = self.registro_universidades.get(codigo_uni)

        if not universidad:
            print(f"Error: No se encontro ninguna universidad con el codigo [{codigo_uni}].")
            return

        nombre_sede = input("Nombre de la Sede: ").strip()
        ubicacion = input("Ciudad / Ubicacion: ").strip()
        direccion = input("Direccion fisica exacta: ").strip()

        if not nombre_sede or not ubicacion or not direccion:
            print("Error: Todos los campos de la sede son obligatorios.")
            return

        nueva_sede = Sede(nombre_sede, ubicacion, direccion)
        print(universidad.agregar_sede(nueva_sede))

    def _seleccionar_sede_interactivo(self) -> Sede:
        codigo_uni = input("Ingrese el codigo de la universidad: ").strip().upper()
        universidad = self.registro_universidades.get(codigo_uni)

        if not universidad:
            print(f"Universidad [{codigo_uni}] no encontrada.")
            return None

        if not universidad.sedes:
            print(f"La universidad {universidad.nombre_uni} no tiene sedes registradas.")
            return None

        print(f"\nSedes disponibles en {universidad.nombre_uni}:")
        for idx, sede in enumerate(universidad.sedes):
            print(f"  [{idx}] Sede: {sede.nombre_sede} ({sede.ubicacion})")
        
        try:
            opcion = int(input("Seleccione el numero de la sede destino: "))
            if opcion < 0 or opcion >= len(universidad.sedes):
                print("Seleccion fuera de rango.")
                return None
            return universidad.sedes[opcion]
        except ValueError:
            print("Entrada invalida. Debe ser un numero entero.")
            return None

    def registrar_facultad(self):
        print("\n--- REGISTRAR FACULTAD EN SEDE ---")
        if not self.registro_universidades:
            print("Error: No hay universidades en el sistema.")
            return

        sede_seleccionada = self._seleccionar_sede_interactivo()
        if not sede_seleccionada:
            return

        nombre_facultad = input("Nombre de la Facultad: ").strip()
        try:
            salones = int(input("Cantidad base de salones teoricos: "))
            laboratorios = int(input("Cantidad base de laboratorios: "))
        except ValueError:
            print("Error: Salones y laboratorios deben ser valores numericos enteros.")
            return

        if not nombre_facultad:
            print("El nombre de la facultad es obligatorio.")
            return

        nueva_facultad = Facultad(nombre_facultad, salones, laboratorios)
        print(sede_seleccionada.agregar_facultad(nueva_facultad))

    def _seleccionar_facultad_interactiva(self):
        sede_seleccionada = self._seleccionar_sede_interactivo()
        if not sede_seleccionada:
            return None

        facultades = sede_seleccionada.mostrar_facultades()
        if isinstance(facultades, str):
            print(facultades)
            return None

        if not facultades:
            print(f"La sede {sede_seleccionada.nombre_sede} no tiene facultades.")
            return None

        print(f"\nFacultades disponibles en {sede_seleccionada.nombre_sede}:")
        for idx, fac in enumerate(facultades):
            print(f"  [{idx}] Facultad: {fac.nombre_facultad}")

        try:
            opcion = int(input("Seleccione el numero de la facultad: "))
            if opcion < 0 or opcion >= len(facultades):
                print("Seleccion fuera de rango.")
                return None
            return facultades[opcion]
        except ValueError:
            print("Entrada invalida.")
            return None

    def vincular_carrera(self):
        print("\n--- VINCULAR CARRERA A FACULTAD ---")
        if not self.registro_universidades:
            print("Error: No hay universidades registradas.")
            return

        facultad_seleccionada = self._seleccionar_facultad_interactiva()
        if not facultad_seleccionada:
            return

        id_carrera = input("Codigo corto unico de la Carrera (Ej: SOFT): ").strip().upper()
        nombre_carrera = input("Nombre completo de la Carrera: ").strip()
        try:
            capacidad = int(input("Capacidad maxima de estudiantes: "))
        except ValueError:
            print("La capacidad debe ser un numero entero.")
            return

        if not id_carrera or not nombre_carrera:
            print("Los campos de identificacion son obligatorios.")
            return

        nueva_carrera = Carrera(id_carrera, nombre_carrera, capacidad)
        print(facultad_seleccionada.importar_carrera(nueva_carrera))

    def generar_aula_automatica(self):
        print("\n--- GENERACION AUTOMATICA DE AULAS ---")
        if not self.registro_universidades:
            print("Error: No hay registros en el sistema.")
            return

        facultad_seleccionada = self._seleccionar_facultad_interactiva()
        if not facultad_seleccionada:
            return

        if not facultad_seleccionada.registro_carreras:
            print("Error: Esta facultad no tiene carreras vinculadas.")
            return

        print("\nCarreras registradas en esta facultad:")
        for codigo, carrera in facultad_seleccionada.registro_carreras.items():
            print(f"  * [{codigo}] -> {carrera.nombre_carrera}")

        codigo_busqueda = input("\nIngrese el codigo de la carrera para asignarle el aula: ").strip().upper()
        
        try:
            capacidad_aula = int(input("Capacidad maxima de alumnos para esta nueva aula: "))
        except ValueError:
            print("La capacidad debe ser un numero entero.")
            return
            
        ubicacion_aula = input("Ubicacion fisica interna (Ej: Edificio Alfa, Piso 2): ").strip()

        if not ubicacion_aula:
            print("La ubicacion fisica es requerida.")
            return

        resultado = facultad_seleccionada.solicitar_nueva_aula(codigo_busqueda, capacidad_aula, ubicacion_aula)
        print(resultado)

    def mostrar_reporte_global(self):
        print("\n======================================================================")
        print("          REPORTE COMPLETO DE INFRAESTRUCTURA INSTITUCIONAL        ")
        print("======================================================================")
        
        if not self.registro_universidades:
            print("   Advertencia: El sistema se encuentra completamente vacio.")
            print("======================================================================\n")
            return

        for cod_uni, uni in self.registro_universidades.items():
            print(f"UNIVERSIDAD: {uni.nombre_uni} [Codigo: {cod_uni}]")
            if not uni.sedes:
                print("   └── Sin sedes registradas.")
            
            for sede in uni.sedes:
                print(f"   └── SEDE: {sede.nombre_sede} ({sede.ubicacion})")
                print(f"       Direccion: {sede.direccion}")
                
                facultades = sede.mostrar_facultades()
                if isinstance(facultades, str) or not facultades:
                    print("       └── Sin facultades registradas.")
                    continue
                
                for fac in facultades:
                    print(f"       └── FACULTAD: {fac.nombre_facultad}")
                    print(f"           Infraestructura Base -> Salones: {fac.infraestructura.salones} | Labs: {fac.infraestructura.laboratorios}")
                    
                    print("           Carreras Academicas:")
                    if not fac.registro_carreras:
                        print("               └── (Ninguna carrera vinculada)")
                    for cod_car, car in fac.registro_carreras.items():
                        print(f"               └── [{cod_car}] {car.nombre_carrera} (Capacidad: {car.capacidad_estudiantil})")
                    
                    print("           Aulas Fisicas Asignadas:")
                    if not fac.infraestructura.lista_aulas:
                        print("               └── (Ninguna aula fisica generada)")
                    for aula in fac.infraestructura.lista_aulas:
                        print(f"               └── ID: [{aula.identifiacadoEntorno}] | Capacidad: {aula.capacidadMaxima} | {aula.obtenerAcceso()}")
        print("======================================================================\n")


if __name__ == "__main__":
    controlador = ControladorConsola()
    
    while True:
        print("============= GESTION UNIVERSITARIA =============")
        print("1. Registrar Universidad")
        print("2. Registrar Sede en una Universidad")
        print("3. Registrar Facultad en una Sede")
        print("4. Vincular Carrera a una Facultad")
        print("5. Generar Aula Fisica Automatica")
        print("6. Visualizar Reporte e Infraestructura Global")
        print("7. Salir")
        print("=================================================")
        
        opcion = input("Seleccione una opcion (1-7): ").strip()
        
        if opcion == "1":
            controlador.registrar_universidad()
        elif opcion == "2":
            controlador.registrar_sede()
        elif opcion == "3":
            controlador.registrar_facultad()
        elif opcion == "4":
            controlador.vincular_carrera()
        elif opcion == "5":
            controlador.generar_aula_automatica()
        elif opcion == "6":
            controlador.mostrar_reporte_global()
        elif opcion == "7":
            print("\nSaliendo del modulo de infraestructura.")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")