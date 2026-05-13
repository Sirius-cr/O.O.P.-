class Sede:
    def __init__(self, nombre_Sede, ubicacion, direccion):
        self.nombre_Sede = nombre_Sede
        self.ubicacion = ubicacion
        self.direccion = direccion
    def modificarDatos():
        pass
    def mostrar_facultades(self):
        return f"facultades de {self.nombre_Sede} son..."
    
class Facultad:
    def __init__(self, carrera, salones, laboratorios):
        self.carrera=carrera
        self.salones=salones
        self.laboratorios=laboratorios

    def registrarAula():
        return f"el aula a sido registrada"
    
    def importarCarrera():
        return f"la carrera a sido importada"
    
class Universidad:
    def __init__(self, nombreUni, codigoUni):
        self.nombreUni=nombreUni
        self.codigoUni=codigoUni

    def modificarDatos(self):
        return f"Estas modificando los datos de {self.nombreUni}"


