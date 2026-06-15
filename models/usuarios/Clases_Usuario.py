from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia):
        self._cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self._correo = correo
        self.__contrasenia = contrasenia

    @property
    def cedula(self): 
        return self._cedula
    
    @abstractmethod
    def ver_perfil(self):
        return f"viendo el perfil" #cada usuario puede ver su perfil
    
    def obtener_cedula(self):
        return self._cedula

    def obtener_nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"
    

    def cambiar_contrasenia(self, contrasenia_actual, nueva_contrasenia):
        if contrasenia_actual != self.__contrasenia:
            return False
            
        if len(nueva_contrasenia) < 8:
            return False
            
        self.__contrasenia = nueva_contrasenia
        return True
    
