from abc import ABC, abstractmethod
from models.usuarios.Clases_Usuario import Usuario

class UsuarioAcademico(Usuario):
    def actualizar_datos_contacto(self, nuevo_correo):
        if "@" not in nuevo_correo:
            #print("Error: Formato de correo inválido.")
            return False
        self._correo = nuevo_correo
        #print("Datos de contacto actualizados en el sistema académico.")
        return True
    
    def ver_horario(self):
        pass
        #falta implementar la logica para horario

    @abstractmethod
    def ver_rendimiento(self):
        #el estudiante vera su rendimiento donde vera cual fue su peor nota en primer o segundo partial
        #el docente al ver rendiminento vera la media de aula y podra comparar calificaciones entre los estudiantes
        pass
    
    @abstractmethod
    def ver_perfil(self):
        return f"viendo el perfil" #cada usuario puede ver su perfil