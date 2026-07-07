Actua como un desarrollador de software profesional y solucioname estos problemas...
1. Como se combinan el coordinador y la carrera? no sería mejor hacer algo para que cuando cree un coordinar en mi base de datos tendría una clave que la una con la carrera? o como está hecho actualmente? respondemelo en este mismo archivo..

2. Como funciona actualemente la asignacion de horarios? como calcula el sistema para que no choquen horarios entre si?



TU RESPUESTA AQUI:

**1. Sobre la relación entre el Coordinador y la Carrera:**
Actualmente, el sistema utiliza una **relación bidireccional (Composición/Asociación) en memoria**, pero está programado de forma algo estática. En el archivo `Clase_Carrera.py` existe el método `asociar_coordinador()` y en `Clase_Coordinador.py` existe `asociar_carrera()`. Ambos métodos se encargan de enlazarse mutuamente, es decir, garantizan que la carrera tenga a ese coordinador y el coordinador tenga a esa carrera. 

Sin embargo, a nivel de **Base de Datos (JSON)**, no existe una clave foránea (como un `id_carrera` dentro de `coordinadores.json`). La vinculación se hace "en caliente" al cargar la aplicación (`app.py`), donde el sistema instancia la "Carrera de Ingeniería de Software" por defecto y luego, al cargar a los coordinadores, ejecuta directamente `coord.asociar_carrera(carrera_software)`. 
**¿Sería mejor tener una clave?** Absolutamente. En un sistema real y escalable, el JSON del coordinador debería tener un campo como `"id_carrera_asignada": "C-001"`. Así, al arrancar, el sistema buscaría la carrera con ese ID y los vincularía automáticamente. Esto permitiría tener múltiples carreras y coordinadores sin tener que "hardcodearlo" en `app.py`.

**2. Sobre la asignación de horarios y el cálculo de choques:**
Actualmente el sistema cuenta con un método llamado `deteccion_colision(self, otro_horario)` dentro de la clase `Horario` (`Clase_Horario.py`). 
Sin embargo, **la validación actual es muy básica**: el sistema *únicamente* compara si el turno de un horario es igual al de otro (`self.turno == otro_horario.turno`). 

No está verificando las horas específicas (`hora_inicio` y `hora_fin`) ni tampoco los días de la semana (por ejemplo, podría haber un turno en la mañana los Lunes y otro en la mañana los Martes que lógicamente no chocarían, pero el sistema actual diría que sí chocan por ser el mismo turno).
Para mejorarlo, el método `deteccion_colision` debería verificar primero si hay coincidencia en los días (intersección de las listas de días) y, si es así, evaluar que los rangos de horas `(inicio1 < fin2)` y `(inicio2 < fin1)` no se superpongan.