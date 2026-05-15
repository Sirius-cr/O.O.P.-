from models.Clase_Universidad import Universidad 
#en tal caso de que se programe la composición lo dejaré de esta manera

class Carrera:
    def __init__(self, id_carrera, nombre_carrera, capacidad_estudiantil, estudiantes_inscritos):
        self._id_carrera = id_carrera #este tipo de atributo es protegido o ( # en uml)
        self.nombre_carrera = nombre_carrera
        self.capacidad_estudiantil = capacidad_estudiantil
        self.estudiantes_inscritos = estudiantes_inscritos
        
    def __crear_lista_estudiantes(self): #esta funcion es privada segun yo se pone asi
        return f"la lista de estudiantes a sido creada, la lista cuenta con {self.estudiantes_inscritos}" 
    
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

class Periodo:
    def __init__(self, fecha_inicio, fecha_final, nombre_periodo):
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.nombre_periodo = nombre_periodo
    

    
        