import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.usuarios.Clase_Docente import Docente
from models.usuarios.Clase_Coordinador import Coordinador


# Crear docentes
docente1 = Docente(
    "0101",
    "Carlos",
    "Lopez",
    "carlos@ups.edu.ec",
    "12345678"
)

docente2 = Docente(
    "0202",
    "Juan",
    "Perez",
    "juan@ups.edu.ec",
    "12345678"
)

docente3 = Docente(
    "0303",
    "Ana",
    "Vera",
    "ana@ups.edu.ec",
    "12345678"
)

# Agregar especialidades
docente1.agregar_especialidad("Matemáticas")
docente1.agregar_especialidad("Física")

docente2.agregar_especialidad("Programación")

docente3.agregar_especialidad("Matemáticas")

# Lista de docentes
lista_docentes = [docente1, docente2, docente3]

# Crear coordinador
coordinador = Coordinador(
    "9999",
    "Pedro",
    "Ruiz",
    "coord@ups.edu.ec",
    "12345678",
    "CO001",
    "2025-01-10"
)

# Buscar docentes de Matemáticas
resultado = coordinador.filtrar_docentes_por_especialidad(
    lista_docentes,
    "Matemáticas"
)

print("DOCENTES DE MATEMÁTICAS")

for docente in resultado:
    print(docente.obtener_nombre_completo())