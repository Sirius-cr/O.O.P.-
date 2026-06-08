class Seccion:
    def __init__(self, id_seccion,entorno_asignado, lista_horarios, capacidad_estudiantil):
        self.id_seccion=id_seccion
        self.docente_asignado=None
        self.entorno_asignado=entorno_asignado
        self.lista_horarios = lista_horarios
        self.capacidad_estudiantil = capacidad_estudiantil
        self.estudiantes_inscritos = []
        self.disponibilidad=True

    def importar_lista(self):
        return f"la lista a sido importada con exito!"
    
    def verificar_cupos_disponibles(self):
        limite_actual= self.calcular_limite_optimo()
        cupos_ocupado=len(self.estudiantes_inscritos)
        if cupos_ocupado < limite_actual:
            return f"La cantidad de cupos disponibles es de:",limite_actual-cupos_ocupado
        else:
            return "No hay cupos disponibles."
            

    def asignar_docente(self,docente):
        self.docente_asignado=docente
        return "Docente asignado al seccion",self.id_seccion       

    def asignar_entorno(self,entorno):
        self.entorno_asignado=entorno
        return f"Entorno asiganado al seccion", {self.id_seccion}

    def liberarCupo(self,estudiante):
        if estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.revome(estudiante)
            return "Cupo liberado"
        return False

    def actualizar_estudiantes_inscritos(self,estudiante):
        if self.verificar_cupos_disponibles():
            if estudiante not in self.estudiantes_inscritos:
                self.estudiantes_inscritos.append(estudiante)
                if self.verificar_cupos_disponibles()==0:
                    self.disponibilidad=False
                return "Estudiante inscrito correctamente."
            return "El estudiante ya esta inscrito"
        self.disponibilidad=False
        return "No existe cupos disponibles."

    def calcular_limite_optimo(self):
        if self.entorno_asignado is None:
            return self.capacidad_estudiantil

        return min(self.capacidad_estudiantil,self.entorno_asignado.capacidadMaxima)
    