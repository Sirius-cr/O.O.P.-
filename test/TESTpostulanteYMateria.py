import sys
import os
# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.Clase_Materia import Materia
from models.Clase_Matricula import Matricula
from models.patrones_diseno.builders.PostulanteBuilder import PostulanteBuilder


materia_prueba = Materia(
    id_materia="SW-402",
    nombre_materia="Programación Orientada a Objetos",
    nota_minima=7.0,
    asistencia_minima=75
)



matricula_prueba = Matricula(
    idMatricula="MATR-2026-001",
    tipoMaticula="Ordinaria",
    fechaMatricula="2026-06-08",
    estadoPagoMatricula=False,
    costeMatricula=120.50
)


postulante_prueba = (
    PostulanteBuilder()
    .con_datos_usuario(
        cedula="1312345678",
        nombres="Juan",
        apellidos="Pérez",
        correo="juan.perez@live.uleam.edu.ec",
        contrasena="password123"
    )
    .con_identificacion_academica(
        idPostulante="POST-001",
        tipoMatricula="Ordinaria"
    )
    .con_detalles_postulacion(
        jornada="Vespertina",
        modalidad="Híbrida",
        cupo=True,
        asistencia=90
    )
    .con_datos_personales(
        celular="0987654321",
        sexo="M",
        etnia="Mestizo",
        discapacidad="Ninguna"
    )
    .build()
)


print("--- 1. Simulando Matrícula de Postulante en Materia ---")
resultado_materia = postulante_prueba.matricularseEnMateria(materia_prueba)
print(resultado_materia)

print("\n--- 2. Simulando Pago de Matrícula ---")
resultado_pago = postulante_prueba.realizarPagoMatricula(matricula_prueba)
print(resultado_pago)
