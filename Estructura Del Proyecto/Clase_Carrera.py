from Clase_Universidad import Universidad 
#en tal caso de que se programe la composición lo dejaré de esta manera

class Carrera:
    def __init__(self, idCarrera, nombreCarrera, capacidadEstudiantil, estudiantesInscritos):
        self._idCarrera=idCarrera #este tipo de atributo es protegido o ( # en uml)
        self.nombreCarrera=nombreCarrera
        self.capacidadEstudiantil=capacidadEstudiantil
        self.estudiantesInscritos=estudiantesInscritos
        
    def __crearListaEstudiantes(self): #esta funcion es privada segun yo se pone asi
        return f"la lista de estudiantes a sido creada, la lista cuenta con {self.estudiantesInscritos}" 
    
class MallaCurricular:
    def __init__(self, codigoMalla, nombreCarrera, areaConocimiento):
        self.codigoMalla=codigoMalla
        self.nombreCarrera=nombreCarrera #aqui puede existir composicion ya que no existe sin uni, aun no la programare
        self.areaConocimiento=areaConocimiento
        
    def agregarMaterias():
        return f"la materia ha sido agregada con éxito"
    
    def mostrarInformacion(self):
        print(f"""
        INFORMACION DE LA MALLA CURRICULAR:
        {"-"*70}
        NOMBRE DE LA CARRERA -> {self.nombreCarrera}
        ÁREA DE CONOCIMIENTO -> {self.areaConocimiento}
        CÓDIGO DE MALLA      -> {self.codigoMalla}
        {"-"*70} 
        """)

        #ABAJO DE CODIGO DE MALLA PUEDE IR ALGO QUE DIGA MATERIAS Y LAS LISTE

class Periodo:
    def __init__(self, fechaInicio, fechaFinal, nombrePeriodo):
        self.fechaInicio=fechaInicio
        self.fechaFinal=fechaFinal
        self.nombrePeriodo=nombrePeriodo
    

    
        