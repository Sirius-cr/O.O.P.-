import sys
import os
import unittest

# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.institucion.Clase_Sede import Sede
from models.institucion.Clase_Facultad import Facultad
from models.institucion.Clase_Carrera import Carrera

class TestInstitucionParametrizado(unittest.TestCase):
    """
    Pruebas unitarias parametrizadas para las clases de la carpeta 'institucion'.
    Aquí puedes modificar las listas de tuplas de parámetros para probar diferentes casos de prueba.
    """

    def test_sede_modificar_datos_parametros(self):
        """
        Prueba parametrizada para el método modificar_datos de la clase Sede.
        Modifica la lista de abajo para añadir tus propios parámetros.
        Formato de la tupla: (nuevo_nombre, nueva_ubicacion, nueva_direccion)
        """
        # ==================== COLOCA TUS PARÁMETROS AQUÍ ====================
        casos_de_prueba = [
            ("Sede Manta", "Manta", "Av. Circunvalación"),
            ("Sede Chone", "Chone", "Calle Bolívar y Atahualpa"),
            ("Sede El Carmen", "El Carmen", "Km 35 Vía a Santo Domingo"),
        ]
        # ====================================================================

        for nombre, ubicacion, direccion in casos_de_prueba:
            with self.subTest(nombre=nombre, ubicacion=ubicacion, direccion=direccion):
                # Instanciamos una sede principal por defecto
                sede = Sede(nombre_sede="Sede Principal", ubicacion="Manta", direccion="Vía San Mateo")
                
                # Ejecutamos la modificación
                sede.modificar_datos(nombre, ubicacion, direccion)
                
                # Asertos para comprobar que los atributos cambiaron correctamente
                self.assertEqual(sede.nombre_sede, nombre)
                self.assertEqual(sede.ubicacion, ubicacion)
                self.assertEqual(sede.direccion, direccion)

    def test_importar_carrera_facultad_parametros(self):
        """
        Prueba parametrizada para importar_carrera de la clase Facultad.
        Modifica la lista de abajo para añadir tus propios parámetros.
        Formato de la tupla: (codigo_carrera, nombre_carrera, capacidad, mensaje_esperado)
        """
        # ==================== COLOCA TUS PARÁMETROS AQUÍ ====================
        casos_de_prueba = [
            ("SOFT", "Ingeniería en Software", 120, "Carrera 'Ingeniería en Software' [SOFT] vinculado a la Facultad de Ciencias Informáticas"),
            ("TI", "Tecnologías de la Información", 80, "Carrera 'Tecnologías de la Información' [TI] vinculado a la Facultad de Ciencias Informáticas"),
            ("AGRO", "Agronomía", 50, "Carrera 'Agronomía' [AGRO] vinculado a la Facultad de Ciencias Informáticas"),
        ]
        # ====================================================================

        for codigo, nombre, capacidad, msg_esperado in casos_de_prueba:
            with self.subTest(codigo=codigo, nombre=nombre, capacidad=capacidad):
                facultad = Facultad("Facultad de Ciencias Informáticas", salones=10, laboratorios=5)
                carrera = Carrera(id_carrera=codigo, nombre_carrera=nombre, capacidad_estudiantil=capacidad)
                
                resultado = facultad.importar_carrera(carrera)
                
                # Comprobamos que el mensaje de retorno sea correcto
                self.assertEqual(resultado, msg_esperado)
                # Comprobamos que la carrera se haya insertado en el diccionario interno por su ID
                self.assertIn(codigo, facultad.registro_carreras)
                self.assertEqual(facultad.registro_carreras[codigo].nombre_carrera, nombre)

if __name__ == '__main__':
    unittest.main()
