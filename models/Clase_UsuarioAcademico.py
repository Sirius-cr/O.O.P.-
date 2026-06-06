from Clases_Usuario import Usuario
#AUN NO SE MODELA BIEN USUARIO ACADEMICO, LE FALTAN ATRIBUTOS Y METODOS
class UsuarioAcademico(Usuario):
    def __init__(self, cedula, nombres, apellidos, correo, contrasena,):
        super().__init__(cedula, nombres, apellidos, correo, contrasena)
        