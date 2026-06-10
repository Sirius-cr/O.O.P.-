from Clase_Materia import Materia
#se deja importado para futuro uso

class MallaCurricular:
    def __init__(self, codigo_malla : str, area_conocimiento: str):
        self.codigo_malla = codigo_malla
        # se remplaza nombre_carrera por una lista que recibe los objetos de materia
        self.lista_materias = []
        self.area_conocimiento = area_conocimiento
        
    def agregar_materias(self, materia_objeto) -> str:
        self.lista_materias.append(materia_objeto)
        return f"la materia ha sido agregada con éxito"
    
    def mostrar_informacion(self):
        print(f"""
        INFORMACION DE LA MALLA CURRICULAR:
        {"-"*70}
        NOMBRE DE LA CARRERA -> {self.nombre_carrera}
        ÁREA DE CONOCIMIENTO -> {self.area_conocimiento}
        CÓDIGO DE MALLA      -> {self.codigo_malla}
        {"-"*70} 
        """)

        #ABAJO DE CODIGO DE MALLA PUEDE IR ALGO QUE DIGA MATERIAS Y LAS LISTE