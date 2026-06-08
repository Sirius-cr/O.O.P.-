from models.Clase_Carrera import Carrera
from models.Clase_Aula import Aula

class InfraestructuraFisca:
    def __init__(self, salones: int, laboratorios: int):
        self.salones = salones
        self.laboratorios = laboratorios
        self.lista_aulas = [] # Guardará las aulas que se hayan registrado

    def añadir_aulas(self, aula_objeto) -> None:
        self.lista_aulas.append(aula_objeto)


class Facultad:
    def __init__(self, nombre_facultad : str, salones: int, laboratorios : int):
        self.nombre_facultad = nombre_facultad
        # integra los salones físicos 
        self.infraestructura = InfraestructuraFisca(salones, laboratorios)        
        # diccionario para buscar carrera por código o nombre
        self.registro_carreras = {}

    def importar_carrera(self, carrera_objeto) -> str:
        codigo = carrera_objeto.id_carrera
        self.registro_carreras[codigo] = carrera_objeto
        return f"Carrera '{carrera_objeto.nombre_carrera}' [{codigo}] vinculado a la {self.nombre_facultad}"
    
    def solicitar_nueva_aula(self, codigo_carrera: str, capacidad_max: int, ubicacion_fisica: str) -> str:
        carrera = self.registro_carreras.get(codigo_carrera)
        if not carrera:
            return " Error: La carrera no pertenece a esta facultad."

        # Calcula cuántas aulas de esta carrera ya existen en la infraestructura
        consecutivo = sum(1 for aula in self.infraestructura.lista_aulas if codigo_carrera in aula.identifiacadoEntorno) + 1
        
        # Pide a la clase Aula que fabrique su propio objeto
        nueva_aula = Aula.crear_aula_automaticamente(carrera, consecutivo, capacidad_max, ubicacion_fisica)
        
        # Guarda el objeto generado en la infraestructura física
        self.infraestructura.añadir_aulas(nueva_aula)
        
        return f"Aula física asignada con éxito: [{nueva_aula.identifiacadoEntorno}] para {carrera.nombre_carrera}."