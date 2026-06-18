import sys
import os

# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.usuarios.Clase_Docente import Docente
from models.usuarios.Clase_Estudiante import Estudiante

def simular_interactivo():
    while True:
        print("\n" + "=" * 50)
        print("    SIMULADOR INTERACTIVO DE REPORTES ULEAM   ")
        print("=" * 50)
        print("1. Simular como DOCENTE (Crear reporte general)")
        print("2. Simular como ESTUDIANTE (Solicitar Certificado)")
        print("3. Simular como ESTUDIANTE (Solicitar Retiro)")
        print("4. Salir")
        print("=" * 50)
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            print("\n--- SIMULANDO COMO DOCENTE ---")
            cedula = input("Cédula [1309876543]: ").strip() or "1309876543"
            nombres = input("Nombres [Maria]: ").strip() or "Maria"
            apellidos = input("Apellidos [Rodriguez]: ").strip() or "Rodriguez"
            correo = input("Correo [maria.rodriguez@uleam.edu.ec]: ").strip() or "maria.rodriguez@uleam.edu.ec"
            contrasenia = input("Contraseña [claveDocente]: ").strip() or "claveDocente"
            especialidad = input("Especialidad [Ingeniería de Software]: ").strip() or "Ingeniería de Software"
            
            docente = Docente(cedula, nombres, apellidos, correo, contrasenia, especialidad)
            
            print("\n--- Datos del reporte a generar ---")
            tipo_de_reporte = input("Tipo de reporte (ej: Solicitud de Equipos): ").strip() or "Solicitud de Equipos"
            formato = input("Formato del documento (PDF/Consola) [PDF]: ").strip() or "PDF"
            contenido = input("Contenido del reporte: ").strip() or "Se solicita el mantenimiento de las aulas."
            
            reporte = docente.realizaReporte(tipo_de_reporte, formato, contenido)
            print("\n" + "=" * 50)
            print("REPORTE GENERADO:")
            print(reporte.imprimir_reporte())
            
        elif opcion == "2":
            print("\n--- SIMULANDO COMO ESTUDIANTE: CERTIFICADO ---")
            cedula = input("Cédula [1312345678]: ").strip() or "1312345678"
            nombres = input("Nombres [Carlos]: ").strip() or "Carlos"
            apellidos = input("Apellidos [Mendoza]: ").strip() or "Mendoza"
            correo = input("Correo [carlos.mendoza@live.uleam.edu.ec]: ").strip() or "carlos.mendoza@live.uleam.edu.ec"
            contrasenia = input("Contraseña [claveEstudiante]: ").strip() or "claveEstudiante"
            id_estudiante = input("ID Estudiante [EST-001]: ").strip() or "EST-001"
            nombre_periodo = input("Periodo Académico [Nivelación 2026]: ").strip() or "Nivelación 2026"
            estado_matricula = input("Estado de Matricula [Matriculado]: ").strip() or "Matriculado"
            tipo_matricula = input("Tipo de Matricula [Ordinaria]: ").strip() or "Ordinaria"
            
            estudiante = Estudiante(cedula, nombres, apellidos, correo, contrasenia, id_estudiante, nombre_periodo, estado_matricula, tipo_matricula)
            
            formato = input("Formato del documento (PDF/Consola) [PDF]: ").strip() or "PDF"
            
            reporte = estudiante.solicitar_certificado(formato)
            print("\n" + "=" * 50)
            print("REPORTE GENERADO:")
            print(reporte.imprimir_reporte())
            
        elif opcion == "3":
            print("\n--- SIMULANDO COMO ESTUDIANTE: RETIRO ---")
            cedula = input("Cédula [1312345678]: ").strip() or "1312345678"
            nombres = input("Nombres [Carlos]: ").strip() or "Carlos"
            apellidos = input("Apellidos [Mendoza]: ").strip() or "Mendoza"
            correo = input("Correo [carlos.mendoza@live.uleam.edu.ec]: ").strip() or "carlos.mendoza@live.uleam.edu.ec"
            contrasenia = input("Contraseña [claveEstudiante]: ").strip() or "claveEstudiante"
            id_estudiante = input("ID Estudiante [EST-001]: ").strip() or "EST-001"
            nombre_periodo = input("Periodo Académico [Nivelación 2026]: ").strip() or "Nivelación 2026"
            estado_matricula = input("Estado de Matricula [Matriculado]: ").strip() or "Matriculado"
            tipo_matricula = input("Tipo de Matricula [Ordinaria]: ").strip() or "Ordinaria"
            
            estudiante = Estudiante(cedula, nombres, apellidos, correo, contrasenia, id_estudiante, nombre_periodo, estado_matricula, tipo_matricula)
            
            motivo = input("Motivo del retiro [Fuerza Mayor]: ").strip() or "Fuerza Mayor"
            formato = input("Formato del documento (PDF/Consola) [Consola]: ").strip() or "Consola"
            
            reporte = estudiante.solicitar_retiro(motivo, formato)
            print("\n" + "=" * 50)
            print("REPORTE GENERADO:")
            print(reporte.imprimir_reporte())
            
        elif opcion == "4":
            print("Saliendo del simulador interactivo.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    simular_interactivo()
