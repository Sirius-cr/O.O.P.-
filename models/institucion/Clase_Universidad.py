# Clase que solo crea la universidad individualmente,
# luego se le asigna la sede, facultad y etc.

class Universidad:
    def __init__(self, nombre_uni: str, codigo_uni: str):
        self.nombre_uni = nombre_uni
        self._codigo_uni = codigo_uni  #Protegido: El código de la institución no debe cambiar
        self.sedes = [] 

    @property
    def codigo_uni(self):
        return self._codigo_uni

    def agregar_sede(self, sede_objeto) -> str:
        #Validación para evitar duplicidad
        if sede_objeto in self.sedes:
            return f"Error: La sede {sede_objeto.nombre_sede} ya está registrada."
            
        self.sedes.append(sede_objeto)
        return f"Sede {sede_objeto.nombre_sede} agregada a la universidad {self.nombre_uni}"

    # Método Mágico para representación legible
    def __str__(self):
        return f"Universidad: {self.nombre_uni} [{self._codigo_uni}] - Sedes: {len(self.sedes)}"