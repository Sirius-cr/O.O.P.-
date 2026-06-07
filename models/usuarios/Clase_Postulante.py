from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico
class Postulante(UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasena, idPostulante, tipoMatricula, celular, jornada, modalidad, cupo, asistencia, sexo, etnia, discapacidad):
        super().__init__(cedula, nombres, apellidos, correo, contrasena)
        self._idPostulante = idPostulante
        self._tipoMatricula = tipoMatricula
        self._celular = celular
        self.jornada = jornada
        self.modalidad = modalidad
        self.cupo = cupo
        self.asistencia = asistencia
        self.sexo = sexo
        self.etnia = etnia
        self.discapacidad = discapacidad
        
    def seleccionarJornada(self):
        pass
    def elegirModalidad(self):
        pass
    def matricularseEnMateria(self):
        pass
    def solicitarRetiro(self):
        pass
    def realizarPagoMatricula(self):
        pass
    # Hereda de UsuarioAcademico pero no se le obliga a implementar calificar()
    def solicitar_retiro(self):
        print("Solicitando retiro de la postulación...")