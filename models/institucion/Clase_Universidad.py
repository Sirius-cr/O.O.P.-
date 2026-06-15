# Clase que solo crea la universidad individualmente,
# luego se le asigna la sede, facultad y etc.

class Universidad:
    def __init__(self, nombreUni, codigoUni):
        self.nombre_uni = nombreUni
        self.codigo_uni = codigoUni
        self.sedes = [] # Lista para guardar las sedes creadas

    def agregar_sede(self, sede_objeto) -> str:
        self.sedes.append(sede_objeto)
        return f"Sede {sede_objeto.nombre_sede} agregada a la universidad {self.nombre_uni}"