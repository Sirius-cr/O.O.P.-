class Seccion:
    def __init__(self, id_seccion, capacidad_estudiantil, materia=None, coordinador=None):
        self.id_seccion = id_seccion
        self.capacidad_estudiantil = capacidad_estudiantil
        self.materia = materia
        self.coordinador = coordinador
        
        # Inicializamos TODAS las listas y variables desde el principio
        self.estudiantes_inscritos = []
        self.lista_horarios = []
        self.docentes = []
        self.entorno_asignado = None
        self.aula_virtual = None
        self.disponibilidad = True

    def agregar_horario(self, horario):
        if horario not in self.lista_horarios:
            self.lista_horarios.append(horario)

    def asignar_aula_virtual(self, aula_virtual):
        self.aula_virtual = aula_virtual
        self.entorno_asignado = aula_virtual
        return f"Aula Virtual asignada a la sección {self.id_seccion}"

    def calcular_limite_optimo(self):
        # Si aún no hay aula asignada, el límite es la capacidad deseada
        if self.entorno_asignado is None:
            return self.capacidad_estudiantil
        
        # Si hay aula, elegimos el número menor entre la sección y el aula física
        return min(self.capacidad_estudiantil, self.entorno_asignado.capacidad_maxima)

    def verificar_cupos_disponibles(self):
        limite_actual = self.calcular_limite_optimo()
        cupos_ocupados = len(self.estudiantes_inscritos)
        
        if cupos_ocupados < limite_actual:
            return True
        else:
            return False

    def importar_lista_horario(self, lista_horario):
        self.lista_horarios = lista_horario
        return self.lista_horarios 
    
    def agregar_docente(self, docente):
        # Desasociar el docente anterior si existía y es diferente
        if self.docentes:
            if self.docentes[0] != docente:
                docente_anterior = self.docentes[0]
                self.docentes.clear()
                if self in docente_anterior.secciones:
                    docente_anterior.secciones.remove(self)
                    
        if docente not in self.docentes:
            self.docentes.append(docente)
            docente.asignar_seccion(self)
        return f"Docente asignado a la sección {self.id_seccion}"

    def asignar_docente(self, docente):
        return self.agregar_docente(docente)

    def asignar_entorno(self, entorno):
        self.entorno_asignado = entorno
        return f"Entorno asignado a la sección {self.id_seccion}"

    def liberar_cupo(self, estudiante):
        if estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.remove(estudiante) # Typo corregido
            
            # Si alguien se retira, automáticamente la sección vuelve a estar disponible
            self.disponibilidad = True 
            return "Cupo liberado"
        return False

    def actualizar_estudiantes_inscritos(self, estudiante):
        # 1. Verificamos si hay espacio general
        if self.verificar_cupos_disponibles():
            # 2. Verificamos que el estudiante no esté duplicado
            if estudiante not in self.estudiantes_inscritos:
                self.estudiantes_inscritos.append(estudiante)
                
                # 3. Volvemos a verificar los cupos DESPUÉS de agregarlo para ver si se llenó
                if not self.verificar_cupos_disponibles():
                    self.disponibilidad = False
                
                return "Estudiante inscrito correctamente."
            return "El estudiante ya está inscrito."
        
        self.disponibilidad = False
        return "No existen cupos disponibles."

    def __len__(self):
        return len(self.estudiantes_inscritos)

    def __bool__(self):
        return True

    def __str__(self):
        materia_name = self.materia.nombre_materia if self.materia else "Sin Materia"
        return f"Sección {self.id_seccion} ({materia_name})"