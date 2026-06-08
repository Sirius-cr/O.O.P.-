from models.usuarios.Clase_Postulante import Postulante
from models.Clase_Materia import Materia
from models.Clase_Matricula import Matricula

# 1. Crear una instancia de Materia
materia_prueba = Materia(
    id_materia="SW-402",
    nombre_materia="Programación Orientada a Objetos",
    nota_minima=7.0,
    asistencia_minima=75
)

# 2. Crear una instancia de Matricula
matricula_prueba = Matricula(
    idMatricula="MATR-2026-001",
    tipoMaticula="Ordinaria",
    fechaMatricula="2026-06-08",
    estadoPagoMatricula=False,
    costeMatricula=120.50
)

# 3. Crear una instancia de Postulante
postulante_prueba = Postulante(
    cedula="1312345678",
    nombres="Juan",
    apellidos="Pérez",
    correo="juan.perez@live.uleam.edu.ec",
    contrasena="password123",
    idPostulante="POST-001",
    tipoMatricula="Ordinaria",
    celular="0987654321",
    jornada="Vespertina",
    modalidad="Híbrida",
    cupo=True,
    asistencia=90,
    sexo="M",
    etnia="Mestizo",
    discapacidad="Ninguna"
)

# 4. Ejecutar pruebas de los métodos
print("--- 1. Simulando Matrícula de Postulante en Materia ---")
resultado_materia = postulante_prueba.matricularseEnMateria(materia_prueba)
print(resultado_materia)

print("\n--- 2. Simulando Pago de Matrícula ---")
resultado_pago = postulante_prueba.realizarPagoMatricula(matricula_prueba)
print(resultado_pago)
