from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, cedula, nombres, apellidos, correo, contrasena):
        self.__cedula = cedula          
        self.nombres = nombres          
        self.apellidos = apellidos      
        self._correo = correo           
        self.__contrasena = contrasena  
    @abstractmethod
    def iniciar_sesion(self):
        """este metodo de iniciar secion es abstracto"""
        pass

    @abstractmethod
    def registrarse(self):
        pass

    @abstractmethod
    def recuperar_contrasena(self):
        pass

class UsuarioAdministrativo(Usuario):
    
    def __init__(self, cedula, nombres, apellidos, correo, contrasena, codigo_administrador):
        super().__init__(cedula, nombres, apellidos, correo, contrasena)
        self._codigo_administrador = codigo_administrador
    #aqui nuevamente escribire los metodos de la clase abstracta para que si los herede
    def iniciar_sesion(self):
        return f"Administrador {self.nombres} ha iniciado sesión en el sistema."

    def registrarse(self):
        return "Procesando registro de nuevo usuario administrativo..."

    def recuperar_contrasena(self):
        return f"Enviando enlace de recuperación al correo: {self._correo}"

    # estos ya serian los metodos propios
    def _consultar_bd_ministerio(self):
        return f"base de datos del ministerio conectada"

    def _matricular_postulante(self):
        pass

    def _promover_estudiante(self):
        pass

    def _asignar_docentes(self):
        pass

    def _aprobar_retiro(self):
        pass

    def _consultar_pagos(self):
        pass

    def _enviar_reporte(self):
        pass

#AUN NO SE MODELA BIEN USUARIO ACADEMICO, LE FALTAN ATRIBUTOS Y METODOS
class UsuarioAcademico(Usuario):
    def __init__(self, cedula, nombres, apellidos, correo, contrasena,):
        super().__init__(cedula, nombres, apellidos, correo, contrasena)

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