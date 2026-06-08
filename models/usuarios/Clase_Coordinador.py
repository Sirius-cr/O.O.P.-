from models.usuarios.Clase_UsuarioAdministrativo import UsuarioAdministrativo
from models.Clase_Periodo import Periodo

class Coordinador(UsuarioAdministrativo):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, idCoordinador, fechaAsignacionCargo):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self._idCoordinador = idCoordinador
        self.fechaAsignacionCargo = fechaAsignacionCargo
        
    def _abrirPeriodoMatricula(self, periodo: Periodo):
        print(f"[COORDINACIÓN] Autorizando la apertura del periodo de matrículas...")
        periodo.iniciarPeriodo()

    def _cerrarPeriodoMatricula(self, periodo: Periodo):
        print(f"[COORDINACIÓN] Solicitando el cierre y clausura oficial del periodo académico...")
        periodo.finalizarPeriodo()

    def aprobarRetiro(self): #Desarrollar lógica de aprobación de retiro de asignatura
        print("Procesando y aprobando solicitud de retiro de asignatura...")
        return True

    def promoverEstudiantes(self): #Desarrollar lógica de promoción académica de estudiantes
        print("Ejecutando proceso masivo de promoción académica para estudiantes aptos...")
        return True

    def asignarDocenteAParalelo(self): #Desarrollar lógica de asignación de docente a paralelo
        print("Asignando carga horaria y docente al paralelo seleccionado...")
        return True