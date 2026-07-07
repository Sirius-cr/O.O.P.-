class Universidad:
    """
    Representa la institución de educación superior principal (Universidad).
    Contiene la lista de sedes pertenecientes a ella.
    """
    def __init__(self, nombreUni, codigoUni):
        """
        Inicializa una nueva instancia de la clase Universidad.

        Parámetros:
        - nombreUni (str): Nombre oficial de la universidad.
        - codigoUni (str): Código o sigla de identificación (ej. "ULEAM").
        """
        self.nombre_uni = nombreUni
        self.codigo_uni = codigoUni
        self.sedes = []  # Lista para almacenar objetos Sede pertenecientes a esta universidad

    def agregar_sede(self, sede_objeto) -> str:
        """
        Agrega una nueva sede física a la universidad.

        Parámetros:
        - sede_objeto (Sede): Objeto de tipo Sede a añadir.

        Retorna:
        - str: Mensaje de confirmación con la sede agregada.
        """
        self.sedes.append(sede_objeto)
        return f"Sede {sede_objeto.nombre_sede} agregada a la universidad {self.nombre_uni}"