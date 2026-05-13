from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, cedula, nombres, apellidos, correo, contraseña):
        self.__cedula = cedula          
        self.nombres = nombres          
        self.apellidos = apellidos      
        self._correo = correo           
        self.__contraseña = contraseña  
    @abstractmethod
    def iniciarSesion(self):
        """este metodo de iniciar secion es abstracto"""
        pass

    @abstractmethod
    def registrarse(self):
        pass

    @abstractmethod
    def recuperarContraseña(self):
        pass