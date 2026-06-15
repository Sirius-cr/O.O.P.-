from models.academico.Clase_Seccion import Seccion

class SeccionBuilder:
    """
    Builder para la clase Seccion que permite la construcción paso a paso
    de objetos de tipo Seccion.
    """
    def __init__(self):
        # Campos requeridos para el constructor de Seccion
        self._id_seccion = None
        self._capacidad_estudiantil = None
        
        # Campos opcionales del constructor de Seccion
        self._materia = None
        self._coordinador = None
        
        # Atributos internos inicializados en Seccion, con soporte para personalización
        self._estudiantes_inscritos = []
        self._lista_horarios = []
        self._docentes = []
        self._entorno_asignado = None
        self._aula_virtual = None
        self._disponibilidad = True

    def con_id_seccion(self, id_seccion):
        """Asigna el identificador de la sección (id_seccion)."""
        self._id_seccion = id_seccion
        return self

    def con_capacidad_estudiantil(self, capacidad_estudiantil):
        """Asigna la capacidad estudiantil de la sección."""
        self._capacidad_estudiantil = capacidad_estudiantil
        return self

    def con_materia(self, materia):
        """Asigna la materia de la sección."""
        self._materia = materia
        return self

    def con_coordinador(self, coordinador):
        """Asigna el coordinador de la sección."""
        self._coordinador = coordinador
        return self

    def con_estudiantes_inscritos(self, estudiantes_inscritos):
        """Asigna la lista inicial de estudiantes inscritos."""
        self._estudiantes_inscritos = list(estudiantes_inscritos) if estudiantes_inscritos is not None else []
        return self

    def agregar_estudiante(self, estudiante):
        """Agrega un estudiante individual a la lista de inscritos."""
        self._estudiantes_inscritos.append(estudiante)
        return self

    def con_lista_horarios(self, lista_horarios):
        """Asigna la lista inicial de horarios."""
        self._lista_horarios = list(lista_horarios) if lista_horarios is not None else []
        return self

    def agregar_horario(self, horario):
        """Agrega un horario individual a la lista de horarios."""
        self._lista_horarios.append(horario)
        return self

    def con_docentes(self, docentes):
        """Asigna la lista inicial de docentes."""
        self._docentes = list(docentes) if docentes is not None else []
        return self

    def agregar_docente(self, docente):
        """Agrega un docente individual a la lista de docentes."""
        self._docentes.append(docente)
        return self

    def con_entorno_asignado(self, entorno_asignado):
        """Asigna el entorno asignado de la sección."""
        self._entorno_asignado = entorno_asignado
        return self

    def con_aula_virtual(self, aula_virtual):
        """Asigna el aula virtual de la sección."""
        self._aula_virtual = aula_virtual
        return self

    def con_disponibilidad(self, disponibilidad):
        """Asigna el estado de disponibilidad de la sección."""
        self._disponibilidad = disponibilidad
        return self

    def build(self) -> Seccion:
        """
        Construye y retorna una instancia de la clase Seccion con los atributos configurados.
        """
        if self._id_seccion is None:
            raise ValueError("El atributo 'id_seccion' es requerido para construir una sección.")
        if self._capacidad_estudiantil is None:
            raise ValueError("El atributo 'capacidad_estudiantil' es requerido para construir una sección.")

        # Crear la instancia usando los parámetros requeridos del constructor
        seccion = Seccion(
            id_seccion=self._id_seccion,
            capacidad_estudiantil=self._capacidad_estudiantil,
            materia=self._materia,
            coordinador=self._coordinador
        )
        
        # Asignar los demás atributos configurados en el builder
        seccion.estudiantes_inscritos = self._estudiantes_inscritos
        seccion.lista_horarios = self._lista_horarios
        seccion.docentes = self._docentes
        seccion.entorno_asignado = self._entorno_asignado
        seccion.aula_virtual = self._aula_virtual
        seccion.disponibilidad = self._disponibilidad
        
        return seccion
