import sys
import os
import unittest
from unittest.mock import patch

# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from App.app import app, secciones, Horario, materias
from models.academico.Clase_Materia import Materia
from models.academico.Clase_Seccion import Seccion

class TestCoordinatorSchedule(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        
        # Guardar secciones y materias originales para restaurarlas después
        self.original_secciones = dict(secciones)
        self.original_materias = dict(materias)
        
        # Configurar materias y secciones de prueba controladas
        self.materia_test = Materia("PROG-TEST", "Materia de Prueba", 7.0, 70)
        materias["PROG-TEST"] = self.materia_test
        
        self.sec1 = Seccion("SEC-TEST-01", 30, self.materia_test)
        self.sec1.lista_horarios = [
            Horario("Matutino", "08:00", "10:00", "PRESENCIAL", ["Lunes", "Miércoles"])
        ]
        
        self.sec2 = Seccion("SEC-TEST-02", 30, self.materia_test)
        self.sec2.lista_horarios = []
        
        secciones.clear()
        secciones["SEC-TEST-01"] = self.sec1
        secciones["SEC-TEST-02"] = self.sec2

    def tearDown(self):
        # Restaurar secciones y materias originales
        secciones.clear()
        secciones.update(self.original_secciones)
        materias.clear()
        materias.update(self.original_materias)

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

    def test_crear_seccion_sin_horario_automatico(self):
        """Prueba que al crear una sección no se le asigne ningún horario por defecto."""
        with self.client.session_transaction() as sess:
            sess['usuario'] = 'coordinador@uleam.edu.ec'
            sess['rol'] = 'coordinador'
            
        data = {
            'id_seccion': 'SEC-NEW-TEST',
            'capacidad': '35',
            'materia_id': 'PROG-TEST'
        }
        
        with patch('App.app.save_db') as mock_save_db:
            response = self.client.post('/coordinator/create_section', data=data)
            self.assertEqual(response.status_code, 200)
            res_json = response.get_json()
            self.assertEqual(res_json['status'], 'success')
            
            # Verificar que la nueva sección se creó y no tiene horarios asignados
            self.assertIn('SEC-NEW-TEST', secciones)
            nueva_sec = secciones['SEC-NEW-TEST']
            self.assertEqual(len(nueva_sec.lista_horarios), 0)

    def test_asignar_horario_manual_y_choque(self):
        """Prueba la asignación manual de horario y la detección de colisiones."""
        with self.client.session_transaction() as sess:
            sess['usuario'] = 'coordinador@uleam.edu.ec'
            sess['rol'] = 'coordinador'
            
        # Caso 1: Asignar un horario que choca con la sección 1 (SEC-TEST-01 tiene Lunes y Miércoles de 08:00-10:00)
        # Vamos a intentar asignar a la sección 2 un horario el Lunes de 09:00-11:00 (choca en la hora 09:00-10:00)
        data_choque = {
            'seccion_id': 'SEC-TEST-02',
            'turno': 'Vespertino',
            'modalidad': 'PRESENCIAL',
            'dias': ['Lunes'],
            'hora_inicio': '09:00',
            'hora_fin': '11:00'
        }
        
        response = self.client.post('/coordinator/assign_schedule', data=data_choque)
        self.assertEqual(response.status_code, 200)
        res_json = response.get_json()
        self.assertEqual(res_json['status'], 'error')
        self.assertIn("El horario choca con la sección SEC-TEST-01", res_json['message'])
        
        # Caso 2: Asignar un horario válido (Lunes de 11:00-13:00, no choca con 08:00-10:00)
        data_valido = {
            'seccion_id': 'SEC-TEST-02',
            'turno': 'Vespertino',
            'modalidad': 'PRESENCIAL',
            'dias': ['Lunes', 'Viernes'],
            'hora_inicio': '11:00',
            'hora_fin': '13:00'
        }
        
        with patch('App.app.save_db') as mock_save_db:
            response = self.client.post('/coordinator/assign_schedule', data=data_valido)
            self.assertEqual(response.status_code, 200)
            res_json = response.get_json()
            self.assertEqual(res_json['status'], 'success')
            
            # Verificar que se asignó correctamente el horario
            sec2 = secciones['SEC-TEST-02']
            self.assertEqual(len(sec2.lista_horarios), 1)
            h = sec2.lista_horarios[0]
            self.assertEqual(h.turno, 'Vespertino')
            self.assertEqual(h.hora_inicio, '11:00')
            self.assertEqual(h.hora_fin, '13:00')
            self.assertEqual(h._modalidad, 'PRESENCIAL')
            self.assertEqual(h.dias, ['Lunes', 'Viernes'])

if __name__ == '__main__':
    unittest.main()
