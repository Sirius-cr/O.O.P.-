class Seccion:
    #en capacidadEsudiantil hay una sobreescritura o ?? está usando un atributo de la clase <Carrera>
    def __init__(self, lista_horarios, capacidad_estudiantil, estudiantes_inscritos):
        self.lista_horarios = lista_horarios
        self.capacidad_estudiantil = capacidad_estudiantil
        self.estudiantes_inscritos = estudiantes_inscritos

    def importar_lista(self):
        return f"la lista a sido importada con exito!"
    