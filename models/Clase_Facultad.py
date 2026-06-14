from models.Clase_Carrera import Carrera

class InfraestructuraFisica:
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
        self.infraestructura = InfraestructuraFisica(salones, laboratorios)        
        # diccionario para buscar carrera por código o nombre
        self.registro_carreras = {}

    def importar_carrera(self, carrera_objeto) -> str:
        codigo = carrera_objeto.id_carrera
        self.registro_carreras[codigo] = carrera_objeto
        return f"Carrera '{carrera_objeto.nombre_carrera}' [{codigo}] vinculado a la {self.nombre_facultad}"