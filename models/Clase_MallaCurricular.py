class MallaCurricular:
    def __init__(self, codigo_malla, nombre_carrera, area_conocimiento):
        self.codigo_malla = codigo_malla
        self.nombre_carrera = nombre_carrera #aqui puede existir composicion ya que no existe sin uni, aun no la programare
        self.area_conocimiento = area_conocimiento
        
    def agregar_materias(self):
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