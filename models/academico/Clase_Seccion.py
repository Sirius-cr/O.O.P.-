class Seccion:
    """
    Representa una sección académica o aula (grupo de estudiantes) asociada a una materia específica.
    Controla el cupo de estudiantes, asignación de docentes, horarios y entornos físicos/virtuales de aprendizaje.
    """

    def __init__(self, id_seccion, capacidad_estudiantil, materia=None, coordinador=None):
        """
        Inicializa una nueva instancia de la clase Seccion.

        Parámetros:
        - id_seccion (str/int): Identificador único de la sección (ej. "A", 101).
        - capacidad_estudiantil (int): Capacidad máxima de estudiantes deseada para la sección.
        - materia (Materia, opcional): Materia académica a la que pertenece la sección.
        - coordinador (Coordinador, opcional): Coordinador académico a cargo.
        """
        self.id_seccion = id_seccion
        self.capacidad_estudiantil = capacidad_estudiantil
        self.materia = materia
        self.coordinador = coordinador
        
        # Inicialización de listas y variables de estado de la sección
        self.estudiantes_inscritos = []  # Lista de estudiantes inscritos en la sección
        self.lista_horarios = []         # Lista de horarios asignados a la sección
        self.docentes = []               # Lista de docentes asignados a la sección (generalmente uno principal)
        self.entorno_asignado = None     # Entorno físico o virtual asignado (aula/laboratorio)
        self.aula_virtual = None         # Referencia al aula virtual asignada
        self.disponibilidad = True       # Estado que indica si la sección aún acepta inscripciones

    def agregar_horario(self, horario):
        """
        Agrega un objeto Horario a la lista de horarios de la sección si no ha sido agregado previamente.

        Parámetros:
        - horario (Horario): El horario a asociar con la sección.
        """
        if horario not in self.lista_horarios:
            self.lista_horarios.append(horario)

    def asignar_aula_virtual(self, aula_virtual):
        """
        Asigna un entorno de aula virtual a la sección.

        Parámetros:
        - aula_virtual (AulaVirtual): El objeto de aula virtual a asignar.

        Retorna:
        - str: Mensaje de confirmación.
        """
        self.aula_virtual = aula_virtual
        self.entorno_asignado = aula_virtual
        return f"Aula Virtual asignada a la sección {self.id_seccion}"

    def calcular_limite_optimo(self):
        """
        Determina el límite máximo real de estudiantes inscritos en la sección.
        Si hay un entorno asignado, se limita por la capacidad máxima del entorno o la sección (el que sea menor).

        Retorna:
        - int: Capacidad óptima o máxima permitida.
        """
        # Si aún no hay aula asignada, el límite es la capacidad deseada
        if self.entorno_asignado is None:
            return self.capacidad_estudiantil
        
        # Si hay aula, elegimos el número menor entre la sección y el aula física/virtual
        return min(self.capacidad_estudiantil, self.entorno_asignado.capacidad_maxima)

    def verificar_cupos_disponibles(self):
        """
        Compara la cantidad actual de estudiantes inscritos con el límite óptimo calculado.

        Retorna:
        - bool: True si hay cupos disponibles (inscritos < límite), False en caso contrario.
        """
        limite_actual = self.calcular_limite_optimo()
        cupos_ocupados = len(self.estudiantes_inscritos)
        
        if cupos_ocupados < limite_actual:
            return True
        else:
            return False

    def importar_lista_horario(self, lista_horario):
        """
        Sobrescribe o importa una lista completa de horarios para la sección.

        Parámetros:
        - lista_horario (list): Nueva lista de objetos Horario.

        Retorna:
        - list: La lista de horarios asignados.
        """
        self.lista_horarios = lista_horario
        return self.lista_horarios 
    
    def agregar_docente(self, docente):
        """
        Asigna un docente a la sección. Desasocia automáticamente al docente previo si
        ya existía uno asignado, manteniendo la consistencia de la asignación.

        Parámetros:
        - docente (Docente): El objeto docente a asignar a la sección.

        Retorna:
        - str: Mensaje de confirmación de la asignación del docente.
        """
        # Desasociar el docente anterior si existía y es diferente del nuevo docente
        if self.docentes:
            if self.docentes[0] != docente:
                docente_anterior = self.docentes[0]
                self.docentes.clear()
                if self in docente_anterior.secciones:
                    docente_anterior.secciones.remove(self)
                    
        # Asigna el nuevo docente si no está ya en la lista y le vincula la sección
        if docente not in self.docentes:
            self.docentes.append(docente)
            docente.asignar_seccion(self)
        return f"Docente asignado a la sección {self.id_seccion}"

    def asignar_docente(self, docente):
        """
        Método alternativo para asignar un docente a la sección (llama a agregar_docente).

        Parámetros:
        - docente (Docente): El docente a asignar.

        Retorna:
        - str: Mensaje de confirmación.
        """
        return self.agregar_docente(docente)

    def asignar_entorno(self, entorno):
        """
        Asigna un entorno físico/aula a la sección.

        Parámetros:
        - entorno (Entorno): Objeto de entorno físico o aula.

        Retorna:
        - str: Mensaje de confirmación.
        """
        self.entorno_asignado = entorno
        return f"Entorno asignado a la sección {self.id_seccion}"

    def liberar_cupo(self, estudiante):
        """
        Remueve a un estudiante inscrito de la sección, liberando su vacante.
        Establece la disponibilidad de la sección en True si se libera espacio.

        Parámetros:
        - estudiante (Estudiante): El estudiante a desinscribir.

        Retorna:
        - str: Mensaje de confirmación si el estudiante estaba inscrito, o False en caso contrario.
        """
        if estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.remove(estudiante)
            
            # Si alguien se retira, automáticamente la sección vuelve a estar disponible
            self.disponibilidad = True 
            return "Cupo liberado"
        return False

    def actualizar_estudiantes_inscritos(self, estudiante):
        """
        Inscribe a un nuevo estudiante en la sección tras validar la disponibilidad de cupo
        y verificar que el estudiante no esté ya registrado en la sección.

        Parámetros:
        - estudiante (Estudiante): El estudiante que se desea inscribir.

        Retorna:
        - str: Mensaje del estado de la inscripción (éxito, duplicado o sin cupos).
        """
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
        
        # Si no hay cupos, actualiza la disponibilidad de la sección a False
        self.disponibilidad = False
        return "No existen cupos disponibles."