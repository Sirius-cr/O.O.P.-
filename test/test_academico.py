import sys
import os
import unittest
from unittest.mock import patch

# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.academico.Clase_Materia import Materia
from models.academico.Clase_Seccion import Seccion
from models.academico.Clase_AulaVirtual import AulaVirtual
from models.usuarios.Clase_Estudiante import Estudiante
from models.patrones_diseno.builders.SeccionBuilder import SeccionBuilder

class TestAcademicoParametrizado(unittest.TestCase):
    """
    Pruebas unitarias parametrizadas para las clases de la carpeta 'academico'.
    Aquí puedes modificar las listas de tuplas de parámetros para probar diferentes casos de prueba.
    """

    def setUp(self):
        # Crear materia base
        self.materia = Materia(
            id_materia="MAT-101",
            nombre_materia="Álgebra Lineal",
            nota_minima=7.0,
            asistencia_minima=70
        )

    def test_calcular_limite_optimo_parametros(self):
        """
        Prueba parametrizada para el método calcular_limite_optimo de la clase Seccion.
        Modifica la lista de abajo para añadir tus propios parámetros.
        Formato de la tupla: (capacidad_seccion, capacidad_aula_virtual_o_None, limite_esperado)
        """
        # ==================== COLOCA TUS PARÁMETROS AQUÍ ====================
        casos_de_prueba = [
            (30, None, 30),      # Sin aula asignada: el límite es la capacidad de la sección
            (30, 40, 30),        # Con aula más grande: el límite es la capacidad de la sección (min de 30 y 40)
            (30, 20, 20),        # Con aula más pequeña: el límite es la capacidad del aula (min de 30 y 20)
            (15, 15, 15),        # Iguales capacidades: el límite es 15
        ]
        # ====================================================================

        for cap_seccion, cap_aula, limite_esperado in casos_de_prueba:
            with self.subTest(cap_seccion=cap_seccion, cap_aula=cap_aula, limite_esperado=limite_esperado):
                seccion = Seccion(id_seccion="SEC-A", capacidad_estudiantil=cap_seccion, materia=self.materia)
                if cap_aula is not None:
                    aula = AulaVirtual(capacidad_maxima=cap_aula, enlace_plataforma="http://virtual.uleam.edu.ec", tipo_plataforma="Teams")
                    seccion.asignar_aula_virtual(aula)
                
                resultado = seccion.calcular_limite_optimo()
                self.assertEqual(
                    resultado, 
                    limite_esperado, 
                    f"Falló calcular_limite_optimo con cap_seccion={cap_seccion}, cap_aula={cap_aula}. Esperaba {limite_esperado} pero obtuve {resultado}."
                )

    def test_verificar_cupos_disponibles_parametros(self):
        """
        Prueba parametrizada para verificar_cupos_disponibles de la clase Seccion.
        Modifica la lista de abajo para añadir tus propios parámetros.
        Formato de la tupla: (capacidad_seccion, num_estudiantes_inscribir, esperado_hay_cupo)
        """
        # ==================== COLOCA TUS PARÁMETROS AQUÍ ====================
        casos_de_prueba = [
            (3, 2, True),   # Capacidad 3, inscribimos 2. Debe haber cupo disponible.
            (3, 3, False),  # Capacidad 3, inscribimos 3. Ya no debe haber cupo disponible.
            (1, 0, True),   # Capacidad 1, inscribimos 0. Debe haber cupo disponible.
            (2, 5, False),  # Capacidad 2, intentamos inscribir 5. No hay cupos.
        ]
        # ====================================================================

        for cap_seccion, num_inscribir, esperado in casos_de_prueba:
            with self.subTest(cap_seccion=cap_seccion, num_inscribir=num_inscribir, esperado=esperado):
                seccion = Seccion(id_seccion="SEC-B", capacidad_estudiantil=cap_seccion, materia=self.materia)
                
                # Inscribir la cantidad especificada de estudiantes de prueba
                for i in range(num_inscribir):
                    estudiante_temp = Estudiante(
                        cedula=f"1312345{i:03d}",
                        nombres=f"Estudiante{i}",
                        apellidos="Prueba",
                        correo=f"est{i}@uleam.edu.ec",
                        contrasenia="pass123",
                        id_estudiante=f"EST-{i:03d}",
                        nombre_periodo="2026-1",
                        estado_matricula="Matriculado",
                        tipo_matricula="Ordinaria"
                    )
                    # Forzar inscripción en la lista directamente para probar verificar_cupos_disponibles de forma aislada
                    if len(seccion.estudiantes_inscritos) < cap_seccion:
                        seccion.estudiantes_inscritos.append(estudiante_temp)
                
                resultado = seccion.verificar_cupos_disponibles()
                self.assertEqual(
                    resultado, 
                    esperado, 
                    f"Falló verificar_cupos_disponibles con cap_seccion={cap_seccion}, inscritos={num_inscribir}. Esperaba {esperado} pero obtuve {resultado}."
                )

    def test_seccion_builder(self):
        """Prueba la construcción de una Sección utilizando SeccionBuilder."""
        aula = AulaVirtual(capacidad_maxima=25, enlace_plataforma="http://test.com", tipo_plataforma="Zoom")
        seccion = (
            SeccionBuilder()
            .con_id_seccion("SEC-100")
            .con_capacidad_estudiantil(30)
            .con_materia(self.materia)
            .con_aula_virtual(aula)
            .con_disponibilidad(True)
            .build()
        )
        self.assertEqual(seccion.id_seccion, "SEC-100")
        self.assertEqual(seccion.capacidad_estudiantil, 30)
        self.assertEqual(seccion.materia, self.materia)
        self.assertEqual(seccion.aula_virtual, aula)
        self.assertTrue(seccion.disponibilidad)
        
        # Probar validación de campos obligatorios
        with self.assertRaises(ValueError):
            SeccionBuilder().con_capacidad_estudiantil(30).build()
        with self.assertRaises(ValueError):
            SeccionBuilder().con_id_seccion("SEC-100").build()

    @patch('builtins.input', side_effect=["SEC-INTERACTIVO", "45"])
    def test_seccion_builder_con_inputs(self, mock_input):
        """Prueba que se puede construir una Sección obteniendo los valores desde inputs simulados del usuario."""
        # Simulamos que le pedimos los datos al usuario por consola (inputs del usuario)
        id_seccion_input = input("Ingrese el ID de la sección: ")
        capacidad_input = int(input("Ingrese la capacidad estudiantil: "))
        
        # Construimos la sección usando el builder con las entradas obtenidas
        seccion = (
            SeccionBuilder()
            .con_id_seccion(id_seccion_input)
            .con_capacidad_estudiantil(capacidad_input)
            .con_materia(self.materia)
            .build()
        )
        
        # Verificamos que se haya construido correctamente con los datos ingresados
        self.assertEqual(seccion.id_seccion, "SEC-INTERACTIVO")
        self.assertEqual(seccion.capacidad_estudiantil, 45)
        self.assertEqual(seccion.materia, self.materia)

if __name__ == '__main__':
    unittest.main()
