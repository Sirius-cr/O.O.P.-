from models.usuarios.Clases_Usuario import Usuario

class UsuarioAcademico(Usuario):
    def actualizarDatosContacto(self, nuevo_correo, nuevo_telefono):
        if "@" not in nuevo_correo:
            print("Error: Formato de correo inválido.")
            return False
        self._correo = nuevo_correo
        self._telefono_contacto = nuevo_telefono
        print("Datos de contacto actualizados en el sistema académico.")
        return True

    def verHorario(self):
        print("Cargando cronograma de actividades académicas...")
        return []

