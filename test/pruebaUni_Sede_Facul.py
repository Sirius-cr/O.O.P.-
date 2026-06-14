import sys
import os
# Añadir el directorio raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.Clase_Universidad import Universidad
from models.Clase_Sede import Sede
from models.Clase_Facultad import Facultad

#Prueba de las Clases Universidad, Sede y Facultad

universidad1 = Universidad("ULEAM", "U001")

sedePrincipal = Sede("Sede Madre", "Planeta Vegeta", "Av. 1 de Sayayin")

facultadMasCabronaAquí = Facultad("Ing. Software", 10, 20)

#llamar metodos

sedePrincipal.agregar_facultad(facultadMasCabronaAquí)
universidad1.agregar_sede(sedePrincipal)

print(f"La universidad {universidad1.nombre_uni} tiene la sede {sedePrincipal.nombre_sede} con la facultad {facultadMasCabronaAquí.nombre_facultad}")
print(f"La sede {sedePrincipal.nombre_sede} esta ubicada en {sedePrincipal.ubicacion} y su direccion es {sedePrincipal.direccion}")
