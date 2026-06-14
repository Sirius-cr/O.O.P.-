from models.usuarios.Clase_UsuarioAdministrativo import UsuarioAdministrativo
from models.Clase_Periodo import Periodo
from models.Clase_Reporte import Reporte

class Coordinador(UsuarioAdministrativo):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, idCoordinador, fechaAsignacionCargo):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.idCoordinador = idCoordinador
        self.fechaAsignacionCargo = fechaAsignacionCargo
        self.carreras = []

    def asociar_carrera(self, carrera):
        if carrera not in self.carreras:
            self.carreras.append(carrera)
            carrera.asociar_coordinador(self)
        
    def abrirPeriodoMatricula(self, periodo: Periodo):
        periodo.iniciarPeriodo()
        # print(f"[COORDINACIÓN] Autorizando la apertura del periodo de matrículas...")
        return True

    def cerrarPeriodoMatricula(self, periodo: Periodo):
        periodo.finalizarPeriodo()
        # print(f"[COORDINACIÓN] Solicitando el cierre y clausura oficial del periodo académico...")
        return True

    def aprobarRetiro(self): #Recibira de la clase Reportes un objeto creado por un estudiante al solicitarRetiro(), este reporte deberá contener la información del estudiante, al aprobar el retiro, el estadoMatricula, del estudiante cambiará de Activo, a Retirado.
        #print("Se ha aprobado el retiro del estudiante {aqui iria el nombre del estudiante}")
        return True

    def asignarDocenteASeccion(self): #Desarrollar lógica de asignación de docente a paralelo

        #print("Asignando carga horaria y docente al paralelo seleccionado...")
        return True
        #Se terminará de programar despues de que seccion se realice correctamente con un builder
