class Sede:
    def __init__(self, nombre_sede, ubicacion, direccion):
        self.nombre_sede = nombre_sede
        self.ubicacion = ubicacion
        self.direccion = direccion

    def modificar_datos(self, nuevo_nombre_Sede : str, nueva_ubicacion : str, nueva_direccion : str):
        self.nombre_sede = nuevo_nombre_Sede
        self.ubicacion = nueva_ubicacion
        self.direccion = nueva_direccion