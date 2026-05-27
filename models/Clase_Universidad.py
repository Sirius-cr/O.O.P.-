   #Separe el codigo en cada uno de sus archivos correspondientes

class Universidad:
    def __init__(self, nombreUni, codigoUni):
        self.nombre_uni = nombreUni
        self.codigo_uni = codigoUni
        
        self.sedes = [] #Lista oara guardar las sedes creadas

    def modificar_datos(self):
        return f"Estas modificando los datos de {self.nombre_uni}"
    
    def agregar_sede(self, sede):
        self.sedes.append(sede)
        return f"Sede {sede.nombre_sede} agregada a la universidad {self.nombre_uni}"


