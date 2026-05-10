class Usuario:
    def __init__(self,cedula,nombre,apellido,correo,contrasenia,codigoUsuario):
        self._cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self._correo=correo
        self.__contrasenia=contrasenia
        self.codigo=codigoUsuario
    @property
    def Contrasenia(self):
        return print(self.__contrasenia)
    @Contrasenia.setter
    def cambiarContrasenia(self,Contrasenia):
        if self.__contrasenia == Contrasenia:
            print("La contraseña es igual.")
        else:
            self.__contrasenia=Contrasenia
            print(self.__contrasenia)

persona1=Usuario(124,"pedro","benitez","@ffjsh",1234,"jd3uyy1")
persona1.Contrasenia
persona1.cambiarContrasenia=321
