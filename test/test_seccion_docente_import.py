import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from App.app import app, secciones, estudiantes
from models.academico.Clase_Materia import Materia
from models.academico.Clase_Seccion import Seccion
from models.usuarios.Clase_Docente import Docente

class TestSeccionDocenteImport(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        
        # Guardar estado original
        self.original_secciones = dict(secciones)
        
        # Mocks para pruebas
        self.materia = Materia("PROG-TEST", "Programacion", 7.0, 70)
        self.seccion = Seccion("SEC-TEST", capacidad_estudiantil=5, materia=self.materia)
        
        self.docente1 = Docente(
            cedula="1312345671", nombres="Docente", apellidos="Uno",
            correo="doc1@uleam.edu.ec", contrasenia="clave123", especialidad="Programacion"
        )
        self.docente2 = Docente(
            cedula="1312345672", nombres="Docente", apellidos="Dos",
            correo="doc2@uleam.edu.ec", contrasenia="clave123", especialidad="Programacion"
        )
        
        secciones.clear()
        secciones["SEC-TEST"] = self.seccion

    def tearDown(self):
        # Restaurar estado original
        secciones.clear()
        secciones.update(self.original_secciones)

    def test_unico_docente_por_seccion(self):
        """Prueba que solo pueda haber un docente por sección."""
        # Asignar primer docente
        self.seccion.asignar_docente(self.docente1)
        self.assertEqual(len(self.seccion.docentes), 1)
        self.assertEqual(self.seccion.docentes[0], self.docente1)
        self.assertIn(self.seccion, self.docente1.secciones)
        
        # Asignar segundo docente
        self.seccion.asignar_docente(self.docente2)
        self.assertEqual(len(self.seccion.docentes), 1)
        self.assertEqual(self.seccion.docentes[0], self.docente2)
        
        # El primer docente debe estar desasociado
        self.assertNotIn(self.seccion, self.docente1.secciones)
        # El segundo docente debe estar asociado
        self.assertIn(self.seccion, self.docente2.secciones)

    @patch('openpyxl.load_workbook')
    def test_importar_estudiantes_limite_capacidad(self, mock_load_workbook):
        """Prueba la validación de capacidad en la importación de estudiantes."""
        # Mock de la hoja de Excel
        mock_wb = MagicMock()
        mock_sheet = MagicMock()
        mock_load_workbook.return_value = mock_wb
        mock_wb.active = mock_sheet
        
        # Fila de cabeceras obligatorias y filas de datos
        headers = ['cedula', 'nombres', 'apellidos', 'correo', 'contrasenia', 'id_estudiante', 'nombre_periodo', 'tipo_matricula']
        
        with self.client.session_transaction() as sess:
            sess['usuario'] = 'coordinador@uleam.edu.ec'
            sess['rol'] = 'coordinador'
            
        # Caso 1: 3 estudiantes (menor que la capacidad máxima de 5) - Debe ser aceptado
        mock_sheet.iter_rows.return_value = [
            headers,
            ['1111111111', 'Est1', 'Ap1', 'est1@uleam.edu.ec', 'pass', 'EST-01', '2026-1', 'Ordinaria'],
            ['2222222222', 'Est2', 'Ap2', 'est2@uleam.edu.ec', 'pass', 'EST-02', '2026-1', 'Ordinaria'],
            ['3333333333', 'Est3', 'Ap3', 'est3@uleam.edu.ec', 'pass', 'EST-03', '2026-1', 'Ordinaria']
        ]
        
        import io
        data1 = {
            'seccion_id': 'SEC-TEST',
            'file': (io.BytesIO(b'dummy'), 'test.xlsx')
        }
        
        with patch('App.app.save_db') as mock_save_db:
            response = self.client.post('/coordinator/import_students', data=data1, content_type='multipart/form-data')
            self.assertEqual(response.status_code, 200)
            res_json = response.get_json()
            self.assertEqual(res_json['status'], 'success')
            self.assertIn("Se importaron con éxito 3 estudiantes", res_json['message'])
            
        # Caso 2: 6 estudiantes (mayor que la capacidad máxima de 5) - Debe ser rechazado
        mock_sheet.iter_rows.return_value = [
            headers,
            ['1111111111', 'Est1', 'Ap1', 'est1@uleam.edu.ec', 'pass', 'EST-01', '2026-1', 'Ordinaria'],
            ['2222222222', 'Est2', 'Ap2', 'est2@uleam.edu.ec', 'pass', 'EST-02', '2026-1', 'Ordinaria'],
            ['3333333333', 'Est3', 'Ap3', 'est3@uleam.edu.ec', 'pass', 'EST-03', '2026-1', 'Ordinaria'],
            ['4444444444', 'Est4', 'Ap4', 'est4@uleam.edu.ec', 'pass', 'EST-04', '2026-1', 'Ordinaria'],
            ['5555555555', 'Est5', 'Ap5', 'est5@uleam.edu.ec', 'pass', 'EST-05', '2026-1', 'Ordinaria'],
            ['6666666666', 'Est6', 'Ap6', 'est6@uleam.edu.ec', 'pass', 'EST-06', '2026-1', 'Ordinaria']
        ]
        
        data2 = {
            'seccion_id': 'SEC-TEST',
            'file': (io.BytesIO(b'dummy'), 'test.xlsx')
        }
        
        response = self.client.post('/coordinator/import_students', data=data2, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        res_json = response.get_json()
        self.assertEqual(res_json['status'], 'error')
        self.assertIn("supera la capacidad de la sección (5)", res_json['message'])

if __name__ == '__main__':
    unittest.main()
