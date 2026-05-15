class Sede:
    def __init__(self, nombre_sede, ubicacion, direccion):
        self.nombre_sede = nombre_sede
        self.ubicacion = ubicacion
        self.direccion = direccion
    def modificar_datos(self):
        pass
    def mostrar_facultades(self):
        return f"facultades de {self.nombre_sede} son..."
    
class Facultad:
    def __init__(self, carrera, salones, laboratorios):
        self.carrera=carrera
        self.salones=salones
        self.laboratorios=laboratorios

    def registrarAula(self):
        return f"el aula a sido registrada"
    
    def registrar_aula(self):
        return f"el aula a sido registrada"
    
    def importar_carrera(self):
        return f"la carrera a sido importada"
    
class Universidad:
    def __init__(self, nombreUni, codigoUni):
        self.nombre_uni = nombreUni
        self.codigo_uni = codigoUni

    def modificar_datos(self):
        return f"Estas modificando los datos de {self.nombre_uni}"
    



