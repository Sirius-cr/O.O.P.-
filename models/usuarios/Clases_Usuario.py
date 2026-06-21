from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia):
        self._cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self._correo = correo
        self.__contrasenia = contrasenia # Atributo privado

    @property
    def cedula(self): 
        return self._cedula

    def obtener_nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"
    
    #Validación
    def _es_contrasenia_valida(self, nueva_contrasenia: str) -> bool:
        if len(nueva_contrasenia) < 8:
            return False
        # Aquí puedes añadir más reglas futuras: 
        # (ej: debe tener números, mayúsculas, etc.)
        return True

    def cambiar_contrasenia(self, contrasenia_actual, nueva_contrasenia):
        #Validar identidad
        if contrasenia_actual != self.__contrasenia:
            return False
            
        # Validar reglas de negocio
        if not self._es_contrasenia_valida(nueva_contrasenia):
            return False
            
        self.__contrasenia = nueva_contrasenia
        return True
