import sys
import os
import unittest

# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from App.app import app, secciones, Horario
from models.academico.Clase_Materia import Materia
from models.academico.Clase_Seccion import Seccion

class TestCoordinatorSchedule(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        
        # Guardar secciones originales para restaurarlas después
        self.original_secciones = dict(secciones)
        
        # Configurar secciones de prueba controladas
        materia_test = Materia("PROG-TEST", "Materia de Prueba", 7.0, 70)
        
        self.sec1 = Seccion("SEC-TEST-01", 30, materia_test)
        self.sec1.lista_horarios = [
            Horario("Matutino", "08:00", "10:00", "PRESENCIAL", ["Lunes", "Miércoles"])
        ]
        
        self.sec2 = Seccion("SEC-TEST-02", 30, materia_test)
        self.sec2.lista_horarios = []
        
        secciones.clear()
        secciones["SEC-TEST-01"] = self.sec1
        secciones["SEC-TEST-02"] = self.sec2

    def tearDown(self):
        # Restaurar secciones originales
        secciones.clear()
        secciones.update(self.original_secciones)

    def test_dashboard_coordinador_secciones_horario(self):
        with self.client.session_transaction() as sess:
            sess['usuario'] = 'coordinador@uleam.edu.ec'
            sess['rol'] = 'coordinador'

        response = self.client.get('/coordinator')
        self.assertEqual(response.status_code, 200)
        
        html_content = response.data.decode('utf-8')
        
        # Debe contener la cabecera "Horario" de la tabla
        self.assertIn("<th>Horario</th>", html_content)
        
        # Debe contener la indicación de "Asignado" con los detalles del horario de la sección 1
        self.assertIn("Asignado", html_content)
        self.assertIn("Matutino (Lunes, Miércoles: 08:00-10:00)", html_content)
        
        # Debe contener la indicación de "Sin Horario" de la sección 2
        self.assertIn("Sin Horario", html_content)

if __name__ == '__main__':
    unittest.main()
