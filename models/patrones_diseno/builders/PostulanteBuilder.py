from models.usuarios.Clase_Postulante import Postulante

class PostulanteBuilder:
    def __init__(self):
        self._cedula = None
        self._nombres = None
        self._apellidos = None
        self._correo = None
        self._contrasena = None
        self._idPostulante = None
        self._tipoMatricula = None
        self._celular = None
        self._jornada = None
        self._modalidad = None
        self._cupo = None #revisar
        self._asistencia = None
        self._sexo = None
        self._etnia = None
        self._discapacidad = None

    def con_datos_usuario(self, cedula, nombres, apellidos, correo, contrasena):
        self._cedula = cedula
        self._nombres = nombres
        self._apellidos = apellidos
        self._correo = correo
        self._contrasena = contrasena
        return self

    def con_identificacion_academica(self, idPostulante, tipoMatricula):
        self._idPostulante = idPostulante
        self._tipoMatricula = tipoMatricula
        return self

    def con_detalles_postulacion(self, jornada, modalidad, cupo, asistencia):
        self._jornada = jornada
        self._modalidad = modalidad
        self._cupo = cupo
        self._asistencia = asistencia
        return self

    def con_datos_personales(self, celular, sexo, etnia, discapacidad):
        self._celular = celular
        self._sexo = sexo
        self._etnia = etnia
        self._discapacidad = discapacidad
        return self

    def build(self) -> Postulante:
        #este es el buider que nos va a retornar todo
        return Postulante(self)
