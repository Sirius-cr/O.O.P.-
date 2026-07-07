import sys
import os
import unittest

# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.usuarios.Clase_Estudiante import Estudiante
from models.usuarios.Clase_Docente import Docente

class TestUsuariosParametrizado(unittest.TestCase):
    """
    Pruebas unitarias parametrizadas para las clases de la carpeta 'usuarios'.
    Aquí puedes modificar las listas de tuplas de parámetros para probar diferentes casos de prueba.
    """

    def setUp(self):
        # Crear instancias base para pruebas
        self.estudiante_base = Estudiante(
            cedula="1312345678",
            nombres="Carlos",
            apellidos="Mendoza",
            correo="carlos.mendoza@live.uleam.edu.ec",
            contrasenia="admin1234",
            id_estudiante="EST-001",
            nombre_periodo="Nivelacion 2026",
            tipo_matricula="Ordinaria"
        )
        self.docente_base = Docente(
            cedula="1309876543",
            nombres="María",
            apellidos="Rodríguez",
            correo="maria.rodriguez@uleam.edu.ec",
            contrasenia="docente2026",
            especialidad="Sistemas"
        )

    def test_cambiar_contrasenia_parametros(self):
        """
        Prueba parametrizada para cambiar_contrasenia de un Usuario.
        Modifica la lista de abajo para añadir tus propios parámetros.
        Formato de la tupla: (contrasenia_actual_proporcionada, nueva_contrasenia, resultado_esperado)
        """
        # ==================== COLOCA TUS PARÁMETROS AQUÍ ====================
        casos_de_prueba = [
            ("admin1234", "nuevaClave123", True),      # Caso válido: contraseña actual correcta y nueva de longitud > 8
            ("admin1234", "corta", False),             # Caso inválido: contraseña nueva muy corta (< 8 caracteres)
            ("claveIncorrecta", "nuevaClave123", False),# Caso inválido: contraseña actual no coincide
            ("admin1234", "12345678", True),           # Caso válido: exactamente 8 caracteres
        ]
        # ====================================================================

        for actual, nueva, esperado in casos_de_prueba:
            with self.subTest(actual=actual, nueva=nueva, esperado=esperado):
                # Restablecemos la contraseña base antes de cada caso
                self.estudiante_base._Usuario__contrasenia = "admin1234"
                
                resultado = self.estudiante_base.cambiar_contrasenia(actual, nueva)
                self.assertEqual(
                    resultado, 
                    esperado, 
                    f"Falló cambiar_contrasenia con actual='{actual}', nueva='{nueva}'. Esperaba {esperado} pero obtuve {resultado}."
                )

    def test_actualizar_datos_contacto_parametros(self):
        """
        Prueba parametrizada para actualizar_datos_contacto de un UsuarioAcademico.
        Modifica la lista de abajo para añadir tus propios parámetros.
        Formato de la tupla: (nuevo_correo, nuevo_telefono, resultado_esperado)
        """
        # ==================== COLOCA TUS PARÁMETROS AQUÍ ====================
        casos_de_prueba = [
            ("juan.nuevo@uleam.edu.ec", "0998887776", True),   # Caso válido: correo con '@'
            ("juan.correo_invalido", "0998887776", False),      # Caso inválido: sin '@'
            ("admin@gmail.com", "0912345678", True),           # Caso válido: con '@'
            ("sin_arroba.com", "0900000000", False),           # Caso inválido: sin '@'
        ]
        # ====================================================================

        for correo, telefono, esperado in casos_de_prueba:
            with self.subTest(correo=correo, telefono=telefono, esperado=esperado):
                resultado = self.docente_base.actualizar_datos_contacto(correo)
                self.assertEqual(
                    resultado, 
                    esperado, 
                    f"Falló actualizar_datos_contacto con correo='{correo}', telefono='{telefono}'. Esperaba {esperado} pero obtuve {resultado}."
                )

if __name__ == '__main__':
    unittest.main()
