from abc import ABC, abstractmethod
from models.usuarios.Clases_Usuario import Usuario

class UsuarioAcademico(Usuario, ABC):
    """
    Clase abstracta que representa a un Usuario con roles de carácter Académico
    (como Estudiantes y Docentes) dentro de la institución.
    Hereda de Usuario y de ABC para definir métodos obligatorios para sus subtipos.
    """
    def actualizar_datos_contacto(self, nuevo_correo):
        """
        Actualiza el correo electrónico del usuario académico, previa validación.

        Parámetros:
        - nuevo_correo (str): Nueva dirección de correo electrónico.

        Retorna:
        - bool: True si se actualiza correctamente, False si el formato es inválido.
        """
        if "@" not in nuevo_correo:
            #print("Error: Formato de correo inválido.")
            return False
        self._correo = nuevo_correo
        #print("Datos de contacto actualizados en el sistema académico.")
        return True
    
    def ver_horario(self):
        """
        Permite visualizar el horario de clases asignado.
        (Pendiente de implementación).
        """
        pass
        #falta implementar la logica para horario

    @abstractmethod
    def ver_rendimiento(self):
        """
        Método abstracto para visualizar el rendimiento académico.
        - En Estudiantes: Muestra notas individuales y peor rendimiento.
        - En Docentes: Muestra estadísticas grupales y medias de aula.
        """
        #el estudiante vera su rendimiento donde vera cual fue su peor nota en primer o segundo partial
        #el docente al ver rendiminento vera la media de aula y podra comparar calificaciones entre los estudiantes
        pass
    
    