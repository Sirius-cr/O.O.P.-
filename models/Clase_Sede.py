class Sede:
    def __init__(self, nombre_sede, ubicacion, direccion):
        self.nombre_sede = nombre_sede
        self.ubicacion = ubicacion
        self.direccion = direccion
    def modificar_datos(self):
        pass
    def mostrar_facultades(self):
        return f"facultades de {self.nombre_sede} son..."
    
    def agregar_facultad(self, facultad):
        return f"facultad {facultad.carrera} agregada a la sede {self.nombre_sede}"