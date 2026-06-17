import sys
import os
import unittest

# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.academico.Clase_Materia import Materia
from models.gestion.Clase_NotaMateria import NotaMateria
from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria

class TestGestionParametrizado(unittest.TestCase):
    """
    Pruebas unitarias parametrizadas para las clases de la carpeta 'gestion'.
    Aquí puedes modificar las listas de tuplas de parámetros para probar diferentes casos de prueba.
    """

    def setUp(self):
        # Crear materia base para asociar a la nota
        self.materia = Materia(
            id_materia="MAT-201",
            nombre_materia="Estructura de Datos",
            nota_minima=7.0,
            asistencia_minima=70
        )

    def test_nota_final_calculo_parametros(self):
        """
        Prueba parametrizada para el cálculo del promedio (nota_final) en NotaMateria.
        Modifica la lista de abajo para añadir tus propios parámetros.
        Formato de la tupla: (parcial1, parcial2, promedio_esperado)
        """
        # ==================== COLOCA TUS PARÁMETROS AQUÍ ====================
        casos_de_prueba = [
            (8.0, 9.0, 8.5),    # Notas estándar
            (10.0, 10.0, 10.0), # Notas máximas
            (0.0, 0.0, 0.0),    # Cero absoluto
            (7.5, 6.5, 7.0),    # Justo en el límite
            (9.25, 8.75, 9.0),  # Con decimales
        ]
        # ====================================================================

        for parcial1, parcial2, esperado in casos_de_prueba:
            with self.subTest(parcial1=parcial1, parcial2=parcial2, esperado=esperado):
                nota_materia = NotaMateria(materia=self.materia, parcial1=parcial1, parcial2=parcial2)
                resultado = nota_materia.nota_final
                self.assertEqual(
                    resultado, 
                    esperado, 
                    f"Falló el promedio de NotaMateria con parcial1={parcial1}, parcial2={parcial2}. Esperaba {esperado} pero obtuve {resultado}."
                )

    def test_esta_aprobado_estado_parametros(self):
        """
        Prueba parametrizada para evaluar el estado de aprobación en NotaMateria.
        Modifica la lista de abajo para añadir tus propios parámetros.
        Formato de la tupla: (parcial1, parcial2, asistencia, estado_esperado)
        """
        # ==================== COLOCA TUS PARÁMETROS AQUÍ ====================
        casos_de_prueba = [
            (7.0, 7.0, 70, EstadoDeAprobacionMateria.MATERIA_APROBADA),   # Justo pasa nota y asistencia
            (10.0, 10.0, 69, EstadoDeAprobacionMateria.MATERIA_REPROBADA), # Nota excelente, pero reprueba por asistencia
            (6.9, 7.0, 95, EstadoDeAprobacionMateria.MATERIA_REPROBADA),   # Asistencia excelente, pero promedio de 6.95 (< 7)
            (9.0, 8.0, 90, EstadoDeAprobacionMateria.MATERIA_APROBADA),   # Pasa holgadamente en ambos criterios
        ]
        # ====================================================================

        for parcial1, parcial2, asistencia, esperado in casos_de_prueba:
            with self.subTest(parcial1=parcial1, parcial2=parcial2, asistencia=asistencia, esperado=esperado):
                nota_materia = NotaMateria(
                    materia=self.materia, 
                    parcial1=parcial1, 
                    parcial2=parcial2, 
                    asistencia=asistencia
                )
                resultado = nota_materia.esta_aprobado
                self.assertEqual(
                    resultado, 
                    esperado, 
                    f"Falló la validación del estado con parcial1={parcial1}, parcial2={parcial2}, asistencia={asistencia}. Esperaba {esperado} pero obtuve {resultado}."
                )

if __name__ == '__main__':
    unittest.main()
