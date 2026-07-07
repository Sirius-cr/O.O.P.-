from models.academico.Clase_Materia import Materia

class MallaCurricular:
    """
    Representa el plan de estudios o malla curricular de una carrera.
    Contiene un conjunto de materias estructuradas asociadas a un área de conocimiento.
    """

    def __init__(self, codigo_malla: str, area_conocimiento: str, carrera=None):
        """
        Inicializa una nueva instancia de la malla curricular.

        Parámetros:
        - codigo_malla (str): Código identificador único de la malla.
        - area_conocimiento (str): Área de conocimiento a la que pertenece (ej. "Tecnología", "Ciencias").
        - carrera (Carrera, opcional): La carrera asociada a esta malla.
        """
        self.codigo_malla = codigo_malla
        self.area_conocimiento = area_conocimiento
        self.lista_materias = []  # Lista que almacenará los objetos Materia pertenecientes a la malla
        self.carrera = carrera

    def agregar_materias(self, materia_objeto):
        """
        Agrega una materia a la lista de materias de la malla curricular.

        Parámetros:
        - materia_objeto (Materia): El objeto Materia a agregar.

        Retorna:
        - str: Mensaje de confirmación del registro.
        """
        self.lista_materias.append(materia_objeto)
        return "Materia agregada correctamente"

    def mostrar_informacion(self):
        """
        Imprime en consola la información detallada de la malla curricular,
        incluyendo su código, área de conocimiento y el listado de materias.
        """
        print(f"""
        MALLA CURRICULAR
        -----------------------------
        Código: {self.codigo_malla}
        Área: {self.area_conocimiento}
        -----------------------------
        Materias:
        """)

        if not self.lista_materias:
            print("   Sin materias")
        else:
            for i, m in enumerate(self.lista_materias, 1):
                print(f"   {i}. {m.nombre_materia}")

    def buscar_materia(self, id_materia):
        """
        Busca una materia dentro de la malla utilizando su identificador único.

        Parámetros:
        - id_materia (str/int): Identificador de la materia a buscar.

        Retorna:
        - Materia: El objeto Materia correspondiente si es encontrado, de lo contrario None.
        """
        for m in self.lista_materias:
            if m.id_materia == id_materia:
                return m
        return None

    def total_materias(self):
        """
        Obtiene la cantidad total de materias que integran la malla curricular.

        Retorna:
        - int: Número de materias.
        """
        return len(self.lista_materias)

    def listar_materias(self):
        """
        Genera una lista con los nombres de todas las materias en la malla curricular.

        Retorna:
        - list: Lista de cadenas (str) con los nombres de las materias.
        """
        return [m.nombre_materia for m in self.lista_materias]