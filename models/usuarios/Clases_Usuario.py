from abc import ABC, abstractmethod

class Usuario(ABC):
    """
    Clase base abstracta que representa a cualquier tipo de Usuario en el sistema.
    Define los atributos y métodos comunes como datos de identificación,
    cambio de contraseña y obtención del nombre completo.
    """
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia):
        """
        Inicializa un nuevo Usuario.

        Parámetros:
        - cedula (str): Cédula de identidad del usuario.
        - nombres (str): Nombres del usuario.
        - apellidos (str): Apellidos del usuario.
        - correo (str): Correo electrónico del usuario.
        - contrasenia (str): Contraseña de acceso del usuario (privada).
        """
        self._cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self._correo = correo
        self.__contrasenia = contrasenia
        
    @property
    def cedula(self): 
        """
        Propiedad para obtener la cédula del usuario.
        """
        return self._cedula
        
    @cedula.setter
    def cedula(self, nueva_cedula):
        """
        Establece una nueva cédula para el usuario.
        """
        self._cedula = nueva_cedula
        
    @property
    def contrasenia(self):
        """
        Propiedad para obtener la contraseña cifrada/privada del usuario.
        """
        return self.__contrasenia
        
    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        """
        Establece una nueva contraseña para el usuario.
        """
        self.__contrasenia = nueva_contrasenia
    
    #Métodos Encapsulado
    def cambiar_contrasenia(self, contrasenia_actual, nueva_contrasenia):
        """
        Permite actualizar la contraseña de acceso, validando la actual y la longitud.

        Parámetros:
        - contrasenia_actual (str): Contraseña actual suministrada.
        - nueva_contrasenia (str): Contraseña nueva sugerida.

        Retorna:
        - bool: True si el cambio fue exitoso, False si falló la validación.
        """
        if contrasenia_actual != self.__contrasenia:
            return False
        if len(nueva_contrasenia) < 8:
            return False
        self.__contrasenia = nueva_contrasenia
        return True
    
    @abstractmethod
    def ver_perfil(self):
        """
        Método abstracto para visualizar los detalles específicos del perfil del usuario.
        Debe ser implementado por las subclases.
        """
        pass 

    def obtener_cedula(self):
        """
        Obtiene de forma explícita la cédula de identidad del usuario.

        Retorna:
        - str: Cédula de identidad.
        """
        return self._cedula

    def obtener_nombre_completo(self):
        """
        Devuelve el nombre completo del usuario concatenando nombres y apellidos.

        Retorna:
        - str: Nombre completo del usuario.
        """
        return f"{self.nombres} {self.apellidos}"