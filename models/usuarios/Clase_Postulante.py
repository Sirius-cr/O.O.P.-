from models.usuarios.Clase_UsuarioAcademico import UsuarioAcademico
from models.Clase_Matricula import Matricula
from models.Clase_Reporte import Reporte

class Postulante(UsuarioAcademico):
    def __init__(self, builder):
        super().__init__(builder._cedula, builder._nombres, builder._apellidos, builder._correo, builder._contrasena)
        self._idPostulante = builder._idPostulante
        self._tipoMatricula = builder._tipoMatricula
        self._celular = builder._celular
        self.jornada = builder._jornada
        self.modalidad = builder._modalidad
        self.cupo = builder._cupo
        self.asistencia = builder._asistencia
        self.sexo =  builder._sexo
        self.etnia = builder._etnia  
        self.discapacidad = builder._discapacidad
        
    def seleccionarJornada(self):
        return f"¿POSTULANTE Elijiendo la jordnada a la que pertenecerá..."
    
    def elegirModalidad(self):
        return f"¿POSTULANTE Elijiendo la modalidad a la que pertenecerá..."
    
    def matricularseEnMateria(self, materia):
        nombre_completo = self.obtener_nombre_completo()
        detalles_materia = f"""
        Nombre de la Materia: {materia.nombre_materia}\n
        ID: {materia.id_materia}\n
        Nota Mínima: {materia.nota_minima}\n
        Asistencia Mínima: {materia.asistencia_minima}%\n"""
        
        return f"{45*"="}\n{nombre_completo} se está matriculando en...\n{45*"="}\n{detalles_materia}"
    
    def solicitarRetiro(self):
        nombre_completo=self.obtener_nombre_completo()
        return f"El postulante {nombre_completo} está solicitando retiro."
        
    def realizarPagoMatricula(self, matricula: Matricula):
        id_mat = matricula.obtener_id_matricula()
        coste = matricula.obtener_coste_matricula()
        return f"{self.obtener_nombre_completo()} ha realizado el pago de la matrícula con ID {id_mat} por un valor de ${coste}."

    # Hereda de UsuarioAcademico pero no se le obliga a implementar calificar()
    def solicitar_retiro(self):
        print("Solicitando retiro de la postulación...")

    def generarReporte(self, formatoDocumento):
        contenido = (
            f"ID Postulante: {self._idPostulante}\n"
            f"Cédula:        {self.cedula}\n"
            f"Jornada:       {self.jornada}\n"
            f"Modalidad:     {self.modalidad}\n"
            f"Cupo:          {self.cupo}"
        )
        return Reporte("Reporte de Postulante", formatoDocumento, self.obtener_nombre_completo(), contenido)