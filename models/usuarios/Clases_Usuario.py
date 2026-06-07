class Usuario():
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia):
        self.__cedula = cedula          
        self._nombres = nombres          
        self._apellidos = apellidos      
        self._correo = correo           
        self.__contrasenia = contrasenia  

    @property
    def cedula(self): #Nos permitira leer la cedula del usuario, pero no modificarla desde fuera de la clase
        return self.__cedula

    def obtener_cedula(self):
        return self.__cedula

    def obtener_nombre_completo(self):
        return f"{self._nombres} {self._apellidos}"
    
    def cambiarContrasenia(self, contrasenia_actual, nueva_contrasenia):
        if contrasenia_actual != self.__contrasenia:
            print("Error: La contraseña actual no es correcta.")
            return False
            
        if len(nueva_contrasenia) < 8:
            print("Error: La nueva contraseña debe tener al menos 8 caracteres.")
            return False
            
        self.__contrasenia = nueva_contrasenia
        print("Contraseña cambiada con éxito.")
        return True
