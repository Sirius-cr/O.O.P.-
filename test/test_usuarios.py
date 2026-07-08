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

    def test_new_delegated_methods(self):
        # 1. Coordinador
        from models.usuarios.Clase_Coordinador import Coordinador
        from models.academico.Clase_Periodo import Periodo
        from models.academico.Clase_Seccion import Seccion
        from models.academico.Clase_Materia import Materia
        from models.academico.Clase_Horario import Horario
        
        periodo = Periodo("Nivelacion 2026", "2026-01-01", "2026-06-01")
        coordinador = Coordinador(
            cedula="1311111111",
            nombres="Pedro",
            apellidos="Pérez",
            correo="pedro.perez@uleam.edu.ec",
            contrasenia="coord123",
            id_coordinador="COORD-02",
            fecha_asignacion_cargo="2026-01-01"
        )
        
        # Test abrir/cerrar periodo
        self.assertTrue(coordinador.abrir_periodo_matricula(periodo))
        self.assertEqual(periodo.estado_periodo, "En curso")
        
        materia = Materia("MAT-002", "Física")
        seccion = Seccion("SEC-B", 30, materia)
        
        # Test asignar_docente_a_seccion with matching specialty
        docente = Docente("1311111112", "Doc", "Prueba", "doc@uleam.edu.ec", "123", "Física")
        self.assertTrue(coordinador.asignar_docente_a_seccion(docente, seccion))
        self.assertIn(docente, seccion.docentes)
        
        # Test asignar_docente_a_seccion mismatch
        docente_mismatch = Docente("1311111113", "Doc2", "Prueba", "doc2@uleam.edu.ec", "123", "Química")
        with self.assertRaises(ValueError):
            coordinador.asignar_docente_a_seccion(docente_mismatch, seccion)
            
        # Test asignar_horario_a_seccion (no collision)
        hor1 = Horario("Matutino", "08:00", "10:00", "PRESENCIAL", ["Lunes"])
        self.assertTrue(coordinador.asignar_horario_a_seccion(seccion, hor1, [seccion]))
        self.assertIn(hor1, seccion.lista_horarios)
        
        # Test collision
        hor2 = Horario("Matutino", "09:00", "11:00", "PRESENCIAL", ["Lunes"])
        seccion2 = Seccion("SEC-C", 30, materia)
        with self.assertRaises(ValueError):
            coordinador.asignar_horario_a_seccion(seccion2, hor2, [seccion])
            
        # Test student enrollment & ver_horario
        self.estudiante_base.inscribir_seccion(seccion)
        self.estudiante_base.historial.crear_nota_materia(materia, periodo)
        self.assertIn(seccion, self.estudiante_base.secciones_asociadas)
        
        horarios = self.estudiante_base.ver_horario()
        self.assertEqual(len(horarios), 1)
        self.assertEqual(horarios[0]["materia"], "Física")
        
        # Test docente colocar_calificacion & tomar_asistencia
        nota_obj = self.estudiante_base.historial.lista_nota_materia[-1]
        docente.colocar_calificacion(nota_obj, 1, 9.5)
        docente.colocar_calificacion(nota_obj, 2, 8.5)
        docente.tomar_asistencia(nota_obj, 90)
        
        self.assertEqual(nota_obj.parcial1, 9.5)
        self.assertEqual(nota_obj.parcial2, 8.5)
        self.assertEqual(nota_obj.asistencia, 90)
        self.assertEqual(nota_obj.ultimo_modificador, docente.obtener_nombre_completo())
        
        # Test ver_rendimiento of student
        peor_nota = self.estudiante_base.ver_rendimiento()
        self.assertEqual(peor_nota, 9.0) # Promedio final de (9.5+8.5)/2 = 9.0
        
        # Test ver_rendimiento of teacher
        rendimiento_doc = docente.ver_rendimiento()
        self.assertEqual(rendimiento_doc, 9.0)

if __name__ == '__main__':
    unittest.main()
