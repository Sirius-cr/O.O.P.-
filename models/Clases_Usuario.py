from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, cedula, nombres, apellidos, correo, contrasena):
        self.__cedula = cedula          
        self.nombres = nombres          
        self.apellidos = apellidos      
        self._correo = correo           
        self.__contrasena = contrasena  
    @abstractmethod
    def iniciar_sesion(self):
        """este metodo de iniciar secion es abstracto"""
        pass

    @abstractmethod
    def registrarse(self):
        pass

    @abstractmethod
    def recuperar_contrasena(self):
        pass





