from models.academico.Clase_Materia import Materia

class MallaCurricular:
    def __init__(self, codigo_malla: str, area_conocimiento: str, carrera=None):
        self.codigo_malla = codigo_malla
        self.area_conocimiento = area_conocimiento
        self.lista_materias = []
        self.carrera = carrera
        self.ofertas_academicas = []

    def agregar_oferta_academica(self, oferta):
        if oferta not in self.ofertas_academicas:
            self.ofertas_academicas.append(oferta)
        
    def agregar_materias(self, materia_objeto) -> str:
        self.lista_materias.append(materia_objeto)
        return "La materia ha sido agregada con éxito"
    
    def mostrar_informacion(self):
        print(f"""
        INFORMACION DE LA MALLA CURRICULAR:
        {"-"*70}
        ÁREA DE CONOCIMIENTO -> {self.area_conocimiento}
        CÓDIGO DE MALLA      -> {self.codigo_malla}
        {"-"*70}
        MATERIAS REGISTRADAS:""")
        
        # Validación: Verificamos si la lista está vacía
        if not self.lista_materias:
            print("        (Aún no hay materias asignadas a esta malla)")
        else:
            # Recorremos la lista y enumeramos cada materia (1, 2, 3...)
            for indice, materia in enumerate(self.lista_materias, start=1):
                # Se asume que el objeto Materia tiene un atributo llamado nombre_materia
                print(f"        {indice}. {materia.nombre_materia}")
        
        print(f"        {"-"*70}\n")