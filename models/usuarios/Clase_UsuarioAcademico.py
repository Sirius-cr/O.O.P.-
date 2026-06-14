from abc import ABC, abstractmethod
from models.usuarios.Clases_Usuario import Usuario

class UsuarioAcademico(Usuario):
    def actualizar_datos_contacto(self, nuevo_correo, nuevo_telefono):
        if "@" not in nuevo_correo:
            #print("Error: Formato de correo inválido.")
            return False
        self._correo = nuevo_correo
        #print("Datos de contacto actualizados en el sistema académico.")
        return True

    @abstractmethod
    def ver_horario(self):
        pass
        #falta implementar la logica para horario