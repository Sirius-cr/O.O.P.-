class Seccion:
    #en capacidadEsudiantil hay una sobreescritura o ?? está usando un atributo de la clase <Carrera>
    def __init__(self, id_seccion, paralelo, docente_asignado,entorno_asignado, lista_horarios, capacidad_estudiantil, estudiantes_inscritos):
        self.id_seccion=id_seccion
        self.paralelo=paralelo
        self.docente_asignado=docente_asignado
        self.entorno_asignado=entorno_asignado
        self.lista_horarios = lista_horarios
        self.capacidad_estudiantil = capacidad_estudiantil
        self.estudiantes_inscritos = estudiantes_inscritos

    def importar_lista(self):
        return f"la lista a sido importada con exito!"
    
    def verificar_cupos_disponibles(self):
        if len(self.estudiantes_inscritos) < self.capacidad_estudiantil:
            cantidadDisponible=self.capacidad_estudiantil-len(self.estudiantes_inscritos)
            return print("La cantidad de cupos disponibles es de:",cantidadDisponible)
        else:
            return print("No hay cupos disponibles.")
            

    def asignar_docente(self,docente):
        self.docente_asignado=docente
        return print("Docente asignado al paralelo",self.paralelo)
        pass

    def asignar_entorno(self,entorno):
        self.entorno_asignado=entorno
        return print("Entorno asiganado al paralelo", self.paralelo)
        pass

    def liberarCupo(self,estudiante):
        if estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.revome(estudiante)
            return print("Cupo liberado")
        return False

    def actualizar_estudiantes_inscritos(self,estudiante):
        if self.verificar_cupos_disponibles():
            if estudiante not in self.estudiantes_inscritos:
                self.estudiantes_inscritos.append(estudiante)
                return "Estudiante inscrito correctamente."
        return "No existe cupos disponibles."

    def calcular_limite_optimo(self):
        if self.entorno_asignado is None:
            return self.capacidad_estudiantil

        return min(self.capacidad_estudiantil,self.entorno_asignado.capacidadMaxima)
    