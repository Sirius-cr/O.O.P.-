#bueno uno de los cambios seria en postulante en donde iria un patron de diseño
### Contexto y Clases Involucradas
*   **Clase a construir:** [Postulante]

### ¿Por qué aplicarlo?
El constructor `__init__` de la clase `Postulante` requiere **15 argumentos** en un orden estricto. Esto se conoce en diseño de software como el *anti-patrón de la lista de parámetros larga*. Es extremadamente fácil cometer errores al instanciarla (por ejemplo, intercambiar el orden de `sexo` y `etnia`, o de `cedula` y `celular`), lo cual genera fallos lógicos difíciles de rastrear.
El patrón **Builder** te permite construir objetos complejos paso a paso de forma legible y segura.

### Cómo podría implementarse
Puedes crear una clase `PostulanteBuilder` que exponga métodos fluidos para ir configurando el objeto poco a poco:

```python
from models.usuarios.Clase_Postulante import Postulante

class PostulanteBuilder:
    def __init__(self):
        # Valores por defecto o temporales
        self._cedula = None
        self._nombres = None
        self._apellidos = None
        self._correo = None
        self._contrasena = None
        self._idPostulante = None
        self._tipoMatricula = "Ordinaria"
        self._celular = ""
        self._jornada = "Matutina"
        self._modalidad = "Presencial"
        self._cupo = False
        self._asistencia = 0
        self._sexo = "M"
        self._etnia = "Mestizo"
        self._discapacidad = "Ninguna"

    def con_datos_usuario(self, cedula, nombres, apellidos, correo, contrasena):
        self._cedula = cedula
        self._nombres = nombres
        self._apellidos = apellidos
        self._correo = correo
        self._contrasena = contrasena
        return self

    def con_identificacion_academica(self, idPostulante, tipoMatricula):
        self._idPostulante = idPostulante
        self._tipoMatricula = tipoMatricula
        return self

    def con_detalles_postulacion(self, jornada, modalidad, cupo, asistencia):
        self._jornada = jornada
        self._modalidad = modalidad
        self._cupo = cupo
        self._asistencia = asistencia
        return self

    def con_datos_personales(self, celular, sexo, etnia, discapacidad):
        self._celular = celular
        self._sexo = sexo
        self._etnia = etnia
        self._discapacidad = discapacidad
        return self

    def build(self) -> Postulante:
        # Retorna la instancia de Postulante totalmente configurada
        return Postulante(
            self._cedula, self._nombres, self._apellidos, self._correo, self._contrasena,
            self._idPostulante, self._tipoMatricula, self._celular, self._jornada,
            self._modalidad, self._cupo, self._asistencia, self._sexo, self._etnia,
            self._discapacidad
        )
```

**Uso práctico al crear un Postulante:**
```python
postulante = (PostulanteBuilder()
              .con_datos_usuario("1312345678", "Juan", "Pérez", "juan.perez@uleam.edu.ec", "pass123")
              .con_identificacion_academica("POST-001", "Ordinaria")
              .con_detalles_postulacion("Vespertina", "Híbrida", True, 90)
              .con_datos_personales("0987654321", "M", "Mestizo", "Ninguna")
              .build())
```
