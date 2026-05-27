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

    

    
        