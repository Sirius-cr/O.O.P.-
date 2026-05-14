class Materia:
    def __init__(self, idMateria, nombreMateria, idDocente, listaEstudiantes, nombrePeriodo, listaInstrumentosEvaluativos, notaMinima, asistenciaMinima):
        self.idMateria=idMateria
        self.nombreMateria=nombreMateria
        self.idDocente=idDocente
        self.listaEstudiantes=listaEstudiantes
        self.nombrePeriodo=nombrePeriodo
        self.listaInstrumentosEvaluativos=listaInstrumentosEvaluativos
        self.notaMinima=notaMinima
        self.asistenciaMinima=asistenciaMinima

    def crearPlanEstudio():
        return f"Felciidades! has creado un plan de estudios con exito"

    def __importarPlanEstudio():
        return f"El plan de estudios a sido importado"
    
    def __subirActividad(self):
        return f"{self.nombreMateria} ==> La actividad a sido subida"
    
    def __eliminarActividad(self):
        return f"{self.nombreMateria} ==> La actvidad a sido borrada"
    
    def __modificarActividad(self):
        return f"{self.nombreMateria} ==> La actividad a sido modificada"
    
    def __calcularPromedio(self):
        return f"el promedio es... CALCULADO XD"
    
class Seccion:
    #en capacidadEsudiantil hay una sobreescritura o ?? esta usando un atributo de la clase <Carrera>
    def __init__(self, listaHorarios, capacidadEstudiantil, estudiantesInscritos):
        self.listaHorarios=listaHorarios
        self.capacidadEstudiantil=capacidadEstudiantil
        self.estudiantesInscritos=estudiantesInscritos

    def importarLista():
        return f"la lista a sido importada con exito!"
    
    