class Sede:
    def __init__(self, nombre_sede, ubicacion, direccion):
        self.nombre_sede = nombre_sede
        self.ubicacion = ubicacion
        self.direccion = direccion
        self.facultades = [] # Lista para guardar las facultades

    def modificar_datos(self, nuevo_nombre_Sede : str, nueva_ubicacion : str, nueva_direccion : str):
        self.nombre_sede = nuevo_nombre_Sede
        self.ubicacion = nueva_ubicacion
        self.direccion = nueva_direccion

    def mostrar_facultades(self):
        return self.facultades
    
    def agregar_facultad(self, facultad_objeto) -> str:
        # Validación para evitar duplicidad por nombre o instancia
        if facultad_objeto in self.facultades:
            return f"Error: La facultad {facultad_objeto.nombre_facultad} ya existe en esta sede."
            
        self.facultades.append(facultad_objeto)
        return f"Facultad {facultad_objeto.nombre_facultad} agregada a la sede {self.nombre_sede}"

    def __str__(self):
        return f"Sede {self.nombre_sede} ({self.ubicacion})"