from models.academico.Clase_Materia import Materia

class MallaCurricular:
    def __init__(self, codigo_malla: str, area_conocimiento: str, carrera=None):
        self.codigo_malla = codigo_malla
        self.area_conocimiento = area_conocimiento
        self.lista_materias = []
        self.carrera = carrera
        self.ofertas_academicas = []

    def agregar_oferta_academica(self,oferta):
        if oferta not in self.ofertas_academicas:
            self.ofertas_academicas.append(oferta)

    def agregar_materias(self, materia_objeto):
        self.lista_materias.append(materia_objeto)
        return "Materia agregada correctamente"

    def mostrar_informacion(self):
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
        for m in self.lista_materias:
            if m.id_materia == id_materia:
                return m
        return None

    def total_materias(self):
        return len(self.lista_materias)

    def listar_materias(self):
        return [m.nombre_materia for m in self.lista_materias]