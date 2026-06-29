import sys
import os
import unittest

# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.usuarios.Clase_Docente import Docente
from models.usuarios.Clase_Estudiante import Estudiante
from models.patrones_diseno.strategy.ReporteStrategy import Reporte

class TestReportesNuevos(unittest.TestCase):
    def setUp(self):
        # Instanciar objetos base para las pruebas (Docente requiere especialidad en esta rama)
        self.docente = Docente(
            cedula="1309876543",
            nombres="Maria",
            apellidos="Rodriguez",
            correo="maria.rodriguez@uleam.edu.ec",
            contrasenia="claveDocente",
            especialidad="Ingeniería de Software"
        )
        self.estudiante = Estudiante(
            cedula="1312345678",
            nombres="Carlos",
            apellidos="Mendoza",
            correo="carlos.mendoza@live.uleam.edu.ec",
            contrasenia="claveEstudiante",
            id_estudiante="EST-001",
            nombre_periodo="Nivelación 2026",
            tipo_matricula="Ordinaria"
        )

    def test_docente_realiza_reporte(self):
        # Probar que el docente genera el reporte correctamente
        reporte = self.docente.realizaReporte(
            tipo_de_reporte="Petición de Equipos",
            formato_documento="PDF",
            contenido="Solicito formalmente 5 computadoras nuevas para el laboratorio de Software."
        )
        self.assertIsInstance(reporte, Reporte)
        self.assertEqual(reporte.tipo_de_reporte, "Petición de Equipos")
        self.assertEqual(reporte.formato_documento, "PDF")
        self.assertEqual(reporte.emisor, "Maria Rodriguez")
        self.assertIn("Solicito formalmente 5 computadoras", reporte.contenido)

        # Probar la salida del reporte formateado
        texto_impreso = reporte.imprimir_reporte()
        self.assertIn("REPORTE ACADÉMICO ULEAM", texto_impreso)
        self.assertIn("Generado por:    Maria Rodriguez", texto_impreso)

    def test_estudiante_solicitar_certificado(self):
        # Probar que el estudiante genera el reporte de certificado
        reporte = self.estudiante.solicitar_certificado(formato_documento="PDF")
        self.assertIsInstance(reporte, Reporte)
        self.assertEqual(reporte.tipo_de_reporte, "Solicitud de Certificado")
        self.assertEqual(reporte.formato_documento, "PDF")
        self.assertEqual(reporte.emisor, "Carlos Mendoza")
        self.assertIn("EST-001", reporte.contenido)
        self.assertIn("Nivelación 2026", reporte.contenido)

    def test_estudiante_solicitar_retiro(self):
        # Probar que el estudiante genera el reporte de retiro
        reporte = self.estudiante.solicitar_retiro(
            motivo="problemas de salud de fuerza mayor",
            formato_documento="Consola"
        )
        self.assertIsInstance(reporte, Reporte)
        self.assertEqual(reporte.tipo_de_reporte, "Solicitud de Retiro")
        self.assertEqual(reporte.formato_documento, "Consola")
        self.assertEqual(reporte.emisor, "Carlos Mendoza")
        self.assertIn("problemas de salud de fuerza mayor", reporte.contenido)

if __name__ == '__main__':
    unittest.main()
