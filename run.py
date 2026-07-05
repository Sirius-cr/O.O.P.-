import os
import sys

# Asegurar que el directorio de trabajo es la raíz del proyecto
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Comprobar la existencia del python del entorno virtual
if sys.platform == "win32":
    venv_python = os.path.join(".venv", "Scripts", "python.exe")
else:
    venv_python = os.path.join(".venv", "bin", "python")

if os.path.exists(venv_python):
    print("---------------------------------------------------------")
    print(" Levantando el Sistema Académico con WebView (en .venv)...")
    print("---------------------------------------------------------")
    os.system(f'"{venv_python}" App/app.py')
else:
    print("[Aviso] No se encontró el ejecutable en .venv. Iniciando con el python del sistema...")
    os.system('python App/app.py')
