from abc import ABC, abstractmethod
import json
import csv

# 1. LA INTERFAZ (Strategy)
# Define el contrato estricto que cualquier formato de reporte debe cumplir.
class IEstrategiaReporte(ABC):
    @abstractmethod
    def generar(self, emisor: str, datos: dict) -> str:
        pass


# 2. ESTRATEGIA CONCRETA: Texto / Consola
# Mantiene el diseño visual que tenías originalmente.
class ReporteConsola(IEstrategiaReporte):
    #Solo voy agregar Atributos para un test luego lo puede eliminar si no es necesario
    def __init__(self, titulo, formato, subtitulo, contenido):
        # Asignamos los parámetros recibidos a atributos del objeto
        self.titulo = titulo
        self.formato = formato
        self.subtitulo = subtitulo
        self.contenido = contenido
    #==================================================
    def generar(self, emisor: str, datos: dict) -> str:
        borde = "=" * 50
        
        # Convierte el diccionario dinámicamente en texto
        contenido_texto = "\n".join([f"  {k.replace('_', ' ').title()}: {v}" for k, v in datos.items()])
        
        return (
            f"\n{borde}\n"
            f"               REPORTE ACADÉMICO ULEAM\n"
            f"{borde}\n"
            f"Formato:         Consola / Texto Plano\n"
            f"Generado por:    {emisor}\n"
            f"{borde}\n"
            f"Contenido:\n"
            f"{contenido_texto}\n"
            f"{borde}\n"
        )


# 3. ESTRATEGIA CONCRETA: JSON (Ideal para exportar datos)
class ReporteJSON(IEstrategiaReporte):
    def generar(self, emisor: str, datos: dict) -> str:
        documento = {
            "institucion": "ULEAM",
            "formato": "JSON",
            "emisor": emisor,
            "contenido": datos
        }
        # Retorna un string formateado como JSON sin pérdida de datos
        return json.dumps(documento, indent=4, ensure_ascii=False)


# 4. EL GESTOR (El Contexto)
# Esta es la clase que usarán los Coordinadores o la Secretaria.
class GestorReportes:
    def __init__(self, estrategia: IEstrategiaReporte):
        self.estrategia = estrategia

    def cambiar_formato(self, nueva_estrategia: IEstrategiaReporte):
        """Permite cambiar el formato del reporte en tiempo de ejecución."""
        self.estrategia = nueva_estrategia

    def emitir_reporte(self, emisor: str, datos: dict):
        return self.estrategia.generar(emisor, datos)
    
# Importacion de Clase_AulaVirtual-

    #EXPORTAR ESTUDIANTES A CSV (SOLO CONECTADOS)
    #Recibe el objeto de aula Virtual para acceder a Estudiantes_conectados
    def exportar_lista_estudiantes_excel(self,AulaVirtual,seccion, nombre_archivo=None):
        #Exporta SOLO los estudiantes que ingresaron al aula virtual a un archivo CSV compatible con Excel.
        if nombre_archivo is None:
            nombre_archivo = f"ingresos_aula_{seccion.id_seccion}.csv"
        if AulaVirtual.estudiantes_conectados:
            return "Error: La lista de estudiantes no ha sido inicializada."
        
        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Encabezados
            writer.writerow([
                "Estudiante",
                "Seccion",
                "Materia",
                "Fecha Exportacion"
            ])

            # Solo estudiantes que realmente ingresaron
            for estudiante in self.estudiantes_conectados:
                writer.writerow([
                    estudiante,
                    seccion.id_seccion,
                    seccion.materia.nombre_materia if seccion.materia else "Sin materia",
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ])

        return f"Archivo generado correctamente: {nombre_archivo}"
