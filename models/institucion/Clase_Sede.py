class Sede:
    """
    Representa una sede física de la universidad.
    Contiene el nombre, ubicación y dirección geográfica de la sede.
    """
    def __init__(self, nombre_sede, ubicacion, direccion):
        """
        Inicializa una nueva instancia de la clase Sede.

        Parámetros:
        - nombre_sede (str): Nombre descriptivo de la sede (ej. "Sede Manta").
        - ubicacion (str): Ciudad o cantón donde se sitúa la sede.
        - direccion (str): Dirección exacta o calles de la sede.
        """
        self.nombre_sede = nombre_sede
        self.ubicacion = ubicacion
        self.direccion = direccion

    def modificar_datos(self, nuevo_nombre_Sede : str, nueva_ubicacion : str, nueva_direccion : str):
        """
        Permite actualizar los datos informativos de la sede.

        Parámetros:
        - nuevo_nombre_Sede (str): Nuevo nombre de la sede.
        - nueva_ubicacion (str): Nueva ubicación.
        - nueva_direccion (str): Nueva dirección.
        """
        self.nombre_sede = nuevo_nombre_Sede
        self.ubicacion = nueva_ubicacion
        self.direccion = nueva_direccion