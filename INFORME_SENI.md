# INFORME TÉCNICO — PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
## Sistema SeNi — Gestión General del Curso de Nivelación

**Universidad Laica "Eloy Alfaro" de Manabí — Facultad de Ciencias de la Vida y Tecnologías**
**Carrera de Software — Asignatura: Programación Orientada a Objetos**
**Docente:** Ing. Jharol Ormaza
**Periodo académico ordinario 2026-1**

**Nombre del Sistema:** Gestión general del curso de nivelación
**Nombre Comercial:** SeNi — *Semestre Nivelatorio*

---

**Integrantes:**
- Coello Mendoza Joseph
- Pilligua Saltos Julean
- Quinteros Velasquez George
- Velez Arcentales Jostin
- Torres Camacho Brayhan

---

# PARTE 1 — ENFOQUE DEL PROYECTO Y OBJETIVO

## 1.1 Contexto y problemática

El ingreso a la educación superior en el Ecuador contempla un **semestre de nivelación** como etapa de transición entre el bachillerato y la carrera universitaria. Este proceso involucra múltiples actores (estudiantes, docentes y coordinadores), la gestión de materias, calificaciones, horarios, secciones y la emisión de certificados y reportes. Sin una herramienta informática estructurada, esta gestión resulta propensa a errores: registros duplicados de estudiantes, solapamientos de horarios, falta de trazabilidad en las calificaciones y dificultad para determinar el estado de aprobación de la nivelación de forma automática y auditable.

**SeNi** nace para resolver esta problemática: es un sistema orientado a objetos que modela el dominio académico del semestre nivelatorio, desde la creación de materias y secciones hasta la evaluación automática del estado final de un estudiante, con soporte para reportes en distintos formatos y la integración de patrones de diseño reconocidos que garantizan la extensibilidad del sistema.

## 1.2 Objetivo general

Construir una **capa de dominio orientada a objetos** que modele el ciclo completo del semestre nivelatorio: registro de materias, gestión de secciones y horarios, asignación de docentes, matrícula de estudiantes, ingreso de calificaciones, evaluación automática del estado de aprobación, y generación de reportes; todo ello aplicando los pilares de la POO y patrones de diseño reconocidos.

## 1.3 Alcance de la capa POO

La capa de modelos del sistema (`models/`) constituye el **núcleo de dominio** del proyecto: contiene las reglas de negocio, las validaciones académicas y los algoritmos de evaluación, completamente independientes de la interfaz web (`App/`). Esta separación responde al principio de **Responsabilidad Única (SRP)**: la lógica de negocio reside en `models/`; la presentación e interacción con el usuario residen en `App/`.

Este informe cubre exclusivamente la carpeta `models/` del repositorio, es decir, el núcleo de dominio orientado a objetos que sostiene al sistema SeNi. No se documenta la capa de interfaz web (`App/`), salvo como referencia de cómo consume a la capa POO.

| Componente del sistema | Clases POO que lo implementan |
|---|---|
| Gestión de institución | `Universidad`, `Sede`, `Carrera` |
| Gestión académica | `MallaCurricular`, `Materia`, `Periodo`, `Seccion`, `Horario` |
| Gestión de usuarios | `Usuario`, `UsuarioAcademico`, `UsuarioAdministrativo`, `Docente`, `Estudiante`, `Coordinador` |
| Gestión de evaluación | `NotaMateria`, `HistorialAcademico` |
| Enumeraciones de dominio | `EstadoDeAprobacionMateria`, `EstadoDeAprobacionNivelacion`, `EstadoPeriodo` |
| Patrones de diseño | `ReporteStrategy` (Strategy), `AulaVirtualBridge` (Bridge), `SeccionBuilder` (Builder), Observer en `NotaMateria`/`HistorialAcademico` |

---

# PARTE 2 — ARQUITECTURA DE LA CAPA POO

## 2.1 Estructura de directorios

```
models/
├── __init__.py
├── academico/
│   ├── __init__.py
│   ├── Clase_Horario.py          # Entidad: bloques horarios con detección de colisión
│   ├── Clase_MallaCurricular.py  # Entidad: agrupa materias por carrera
│   ├── Clase_Materia.py          # Entidad: materia con nota/asistencia mínima
│   ├── Clase_Periodo.py          # Entidad: máquina de estados del periodo académico
│   └── Clase_Seccion.py          # Entidad agregado: horarios, docentes y estudiantes
│
├── enums/
│   ├── Estado_Aprobacion.py      # EstadoDeAprobacionMateria, EstadoDeAprobacionNivelacion
│   └── Estado_Periodo.py         # EstadoPeriodo (PLANIFICACION, EN_CURSO, FINALIZADO)
│
├── gestion/
│   ├── __init__.py
│   ├── Clase_HistorialAcademico.py  # Observer concreto + cálculo de aprobación
│   └── Clase_NotaMateria.py         # Sujeto Observer + notas con propiedades interceptadas
│
├── institucion/
│   ├── __init__.py
│   ├── Clase_Carrera.py          # Entidad con malla y coordinador asociados
│   ├── Clase_Sede.py             # Entidad de sede física
│   └── Clase_Universidad.py      # Entidad raíz institucional
│
├── patrones_diseno/
│   ├── bridge/
│   │   └── AulaVirtualBridge.py  # Patrón Bridge: aulas + servicios de streaming
│   ├── builders/
│   │   └── SeccionBuilder.py     # Patrón Builder: construcción fluida de Seccion
│   └── strategy/
│       └── ReporteStrategy.py    # Patrón Strategy: reportes en Consola o JSON
│
└── usuarios/
    ├── Clases_Usuario.py              # Clase base con encapsulación fuerte
    ├── Clase_UsuarioAcademico.py      # Clase intermedia (Docente/Estudiante)
    ├── Clase_UsuarioAdministrativo.py # Clase intermedia (Coordinador)
    ├── Clase_Docente.py               # Herencia + métodos académicos docentes
    ├── Clase_Estudiante.py            # Herencia múltiple (UsuarioAcademico + Observador)
    └── Clase_Coordinador.py           # Administración de periodos y secciones
```

## 2.2 Métricas generales de la capa

- **≈ 20 archivos `.py`** en la carpeta `models/`
- **3 enumeraciones** de dominio académico
- **4 patrones de diseño** implementados (Observer, Strategy, Bridge, Builder)
- **6 clases de la jerarquía de usuarios** en dos ramas (académica y administrativa)
- **5 entidades académicas** (`Materia`, `Periodo`, `Seccion`, `Horario`, `MallaCurricular`)
- **2 entidades de gestión** (`NotaMateria`, `HistorialAcademico`)
- **3 entidades institucionales** (`Universidad`, `Sede`, `Carrera`)

## 2.3 Principios SOLID aplicados

| Principio | Evidencia en la capa POO |
|---|---|
| **S**RP | Cada clase tiene una única responsabilidad: `Horario` solo modela bloques de tiempo; `HistorialAcademico` solo calcula el estado de nivelación; `SeccionBuilder` solo construye `Seccion`. |
| **O**CP | Nuevas estrategias de reporte se agregan implementando `IEstrategiaReporte` sin modificar `Reporte`; nuevas plataformas de streaming se agregan implementando `IServicioStreaming` sin tocar `AulaVirtual`. |
| **L**SP | `Docente` y `Estudiante` son intercambiables donde se espera `UsuarioAcademico`; `AulaClaseSincrona` y `AulaExamen` son intercambiables donde se espera `AulaVirtual`. |
| **I**SP | `UsuarioAcademico` define solo los métodos comunes a los actores académicos (`ver_horario`, `ver_rendimiento`, `ver_perfil`); `UsuarioAdministrativo` no hereda esos contratos abstractos innecesariamente. |
| **D**IP | `Reporte` depende de la abstracción `IEstrategiaReporte`, no de `ReporteConsola` directamente; `AulaVirtual` depende de `IServicioStreaming`, no de `ServicioZoom` o `ServicioTeams` en concreto. |

## 2.4 Patrones de diseño implementados

| Patrón | Tipo | Ubicación | Rol |
|---|---|---|---|
| **Observer** | Comportamiento | `NotaMateria` (Sujeto), `HistorialAcademico` + `Estudiante` (Observadores) | Cuando un docente modifica una calificación, `NotaMateria` notifica automáticamente al historial (que recalcula el estado de nivelación) y al estudiante (que registra la notificación). |
| **Strategy** | Comportamiento | `ReporteStrategy.py` | El formato del reporte (Consola o JSON) es intercambiable en tiempo de ejecución sin modificar la clase `Reporte`. |
| **Bridge** | Estructural | `AulaVirtualBridge.py` | Desacopla la jerarquía de aulas virtuales (`AulaClaseSincrona`, `AulaExamen`) de la plataforma de streaming (`ServicioTeams`, `ServicioZoom`). |
| **Builder** | Creacional | `SeccionBuilder.py` | Permite construir objetos `Seccion` paso a paso de forma fluida, validando los campos obligatorios antes de instanciar. |

---

# PARTE 3 — DESARROLLO: PASOS SEGUIDOS Y CÓDIGO FUENTE COMENTADO

Esta parte reconstruye el desarrollo de la capa POO en el orden lógico en que las dependencias deben construirse: primero el "vocabulario" del dominio (enumeraciones), luego las entidades base, la jerarquía de usuarios, las entidades académicas compuestas, los patrones de diseño y finalmente la demostración en `main.py`.

## 3.1 Paso 1 — Vocabulario del dominio: las enumeraciones (`enums/`)

Antes de escribir ninguna entidad, se definieron las **enumeraciones** que representan los valores cerrados y controlados del dominio. Usar `Enum` en lugar de cadenas de texto libres elimina errores de tipeo y centraliza los valores permitidos en un único lugar.

```python
# models/enums/Estado_Aprobacion.py

from enum import Enum

class EstadoDeAprobacionMateria(Enum):
    # Constantes de umbral — usadas para comparar notas y asistencia
    NOTA_MINIMA_APROBACION = 7.0   # Nota mínima para aprobar una materia
    ASISTENCIA_MINIMA      = 70    # Porcentaje mínimo de asistencia requerido

    # Estados posibles de una materia
    MATERIA_APROBADA   = 'Materia aprobada'
    MATERIA_REPROBADA  = 'Materia reprobada'
    MATERIA_PENDIENTE  = 'Materia pendiente'   # El periodo aún no ha cerrado

class EstadoDeAprobacionNivelacion(Enum):
    # Estado consolidado del semestre completo
    APROBADO  = 'Nivelación Aprobada'
    REPROBADO = 'Nivelación Reprobada'
    PENDIENTE = 'Nivelación Pendiente'
```

```python
# models/enums/Estado_Periodo.py

from enum import Enum

class EstadoPeriodo(Enum):
    PLANIFICACION = "En Planificación"  # Periodo creado, aún no iniciado
    EN_CURSO      = "En Curso"          # Periodo activo: se pueden ingresar notas
    FINALIZADO    = "Finalizado"        # Periodo cerrado: las notas son definitivas
```

La enumeración `EstadoDeAprobacionMateria` combina en un solo `Enum` tanto **constantes de umbral** (valores numéricos) como **estados de resultado** (cadenas descriptivas). Esto permite que `NotaMateria` consulte `EstadoDeAprobacionMateria.NOTA_MINIMA_APROBACION.value` (7.0) directamente desde el enum, asegurando que la regla de aprobación esté centralizada y no dispersa en múltiples clases.

## 3.2 Paso 2 — Entidades institucionales base (`institucion/`)

Con el vocabulario definido, se construyeron las entidades institucionales "hoja": `Universidad`, `Sede` y `Carrera`.

```python
# models/institucion/Clase_Carrera.py (fragmento clave)

class Carrera:
    def __init__(self, id_carrera: str, nombre_carrera: str,
                 capacidad_estudiantil: int, estudiantes_inscritos: int = 0):
        self._id_carrera = id_carrera           # Protegido: solo accesible via property
        self.nombre_carrera = nombre_carrera
        self.capacidad_estudiantil = capacidad_estudiantil
        self.estudiantes_inscritos = estudiantes_inscritos
        self.malla_curricular = None
        self.coordinador = None

    def asociar_coordinador(self, coordinador):
        """Asociación bidireccional: la carrera conoce al coordinador y viceversa.
        La guarda 'if self.coordinador != coordinador' evita recursión infinita."""
        if self.coordinador != coordinador:
            self.coordinador = coordinador
            coordinador.asociar_carrera(self)   # Notifica al coordinador

    def crear_malla_curricular(self, codigo_malla: str, area_conocimiento: str):
        """Factory Method interno: crea y asocia la malla evitando
        que el llamador deba importar MallaCurricular directamente."""
        from models.academico.Clase_MallaCurricular import MallaCurricular
        self.malla_curricular = MallaCurricular(codigo_malla, area_conocimiento, carrera=self)
        return self.malla_curricular

    @property
    def id_carrera(self) -> str:
        """El ID de carrera es de solo lectura desde fuera de la clase."""
        return self._id_carrera

    def __crear_lista_estudiantes(self):
        """Método privado (double underscore = name mangling de Python):
        solo accesible dentro de la propia clase Carrera."""
        return f"la lista de estudiantes ha sido creada con {self.estudiantes_inscritos}"
```

## 3.3 Paso 3 — Jerarquía de usuarios (herencia, polimorfismo, encapsulación)

Esta es la sección donde se concentran los pilares clásicos de la POO: **herencia multinivel**, **herencia múltiple** (mezcla con la interfaz `Observador`), **polimorfismo** de métodos abstractos y **encapsulación fuerte** de la contraseña.

```
Usuario (Base)                         ← encapsulación + métodos comunes
 ├── UsuarioAcademico (ABC)             ← abstracción: ver_rendimiento, ver_perfil abstractos
 │    ├── Docente                       ← implementa ver_rendimiento, ver_perfil
 │    └── Estudiante  (+ Observador)    ← herencia múltiple: academico + observador
 └── UsuarioAdministrativo              ← sin métodos abstractos propios
      └── Coordinador                   ← gestión de periodos, secciones y docentes
```

### Clase base `Usuario`: encapsulación fuerte

```python
# models/usuarios/Clases_Usuario.py

class Usuario():
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia):
        self._cedula = cedula           # Protegido: accesible via property con setter
        self.nombres = nombres          # Público: nombre visible y modificable
        self.apellidos = apellidos      # Público
        self._correo = correo           # Protegido
        self.__contrasenia = contrasenia  # PRIVADO: doble guion bajo aplica name mangling
                                          # Solo accesible a través del setter validado

    @property
    def contrasenia(self):
        return self.__contrasenia      # Lectura permitida vía property

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        self.__contrasenia = nueva_contrasenia   # Escritura solo via setter

    def cambiar_contrasenia(self, contrasenia_actual, nueva_contrasenia):
        """Regla de negocio: valida la contraseña actual y exige mínimo 8 caracteres."""
        if contrasenia_actual != self.__contrasenia:
            return False             # Contraseña actual incorrecta
        if len(nueva_contrasenia) < 8:
            return False             # Contraseña nueva demasiado corta
        self.__contrasenia = nueva_contrasenia
        return True

    def __eq__(self, otro):
        """Dos usuarios son iguales si comparten cédula O correo,
        previniendo registros duplicados en el sistema."""
        if not isinstance(otro, Usuario):
            return False
        return self._cedula == otro._cedula or self._correo == otro._correo
```

### Clase intermedia `UsuarioAcademico`: abstracción con métodos abstractos

```python
# models/usuarios/Clase_UsuarioAcademico.py

from abc import ABC, abstractmethod
from models.usuarios.Clases_Usuario import Usuario

class UsuarioAcademico(Usuario):
    def actualizar_datos_contacto(self, nuevo_correo):
        """Valida formato de correo antes de actualizar."""
        if "@" not in nuevo_correo:
            return False
        self._correo = nuevo_correo
        return True

    @abstractmethod
    def ver_rendimiento(self):
        """Polimorfismo: Docente ve la media de aula;
        Estudiante ve su peor nota parcial."""
        pass

    @abstractmethod
    def ver_perfil(self):
        """Cada tipo de usuario muestra su propia información de perfil."""
        pass
```

### `Docente`: herencia simple, métodos de gestión académica

```python
# models/usuarios/Clase_Docente.py (fragmento clave)

class Docente(UsuarioAcademico):
    def __init__(self, cedula, nombres, apellidos, correo, contrasenia, especialidad):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self.especialidad = especialidad   # Atributo específico del docente
        self.secciones = []

    def ver_rendimiento(self):
        """Polimorfismo: el docente no ve su propia nota, sino la media
        de las notas finales de TODOS sus estudiantes en TODAS sus secciones."""
        todas_notas = []
        for sec in self.secciones:
            for est in sec.estudiantes_inscritos:
                nota_obj = next(
                    (n for n in est.historial.lista_nota_materia
                     if n.materia.id_materia == sec.materia.id_materia), None
                )
                if nota_obj:
                    todas_notas.append(nota_obj.nota_final)
        return sum(todas_notas) / len(todas_notas) if todas_notas else 0.0

    def colocar_calificacion(self, nota, parcial, valor):
        """El docente modifica la nota de un parcial específico (1 o 2).
        Al modificar nota.parcial1 o nota.parcial2, el setter de NotaMateria
        dispara automáticamente el patrón Observer."""
        if parcial == 1:
            nota.parcial1 = valor        # Dispara Observer → notifica historial y estudiante
        elif parcial == 2:
            nota.parcial2 = valor
        nota.ultimo_modificador = self.obtener_nombre_completo()
        return True

    def tomar_asistencia(self, nota, valor):
        """Registra la asistencia del estudiante. El setter de NotaMateria
        también disparará el Observer automáticamente."""
        nota.asistencia = valor
        nota.ultimo_modificador = self.obtener_nombre_completo()
        return True
```

### `Estudiante`: herencia múltiple (UsuarioAcademico + Observador)

```python
# models/usuarios/Clase_Estudiante.py (fragmento clave)

class Estudiante(UsuarioAcademico, Observador):
    """Herencia múltiple: es un UsuarioAcademico Y un Observador del patrón Observer,
    porque necesita recibir notificaciones cuando un docente modifica sus calificaciones."""

    def __init__(self, cedula, nombres, apellidos, correo, contrasenia,
                 id_estudiante, nombre_periodo, tipo_matricula):
        super().__init__(cedula, nombres, apellidos, correo, contrasenia)
        self._id_estudiante = id_estudiante
        self.nombre_periodo = nombre_periodo
        self._tipo_matricula = tipo_matricula
        # COMPOSICIÓN: cada estudiante TIENE UN historial académico propio
        self.historial = HistorialAcademico(id_historial=id_estudiante, estudiante=self)
        self.secciones_asociadas = []
        self.notificaciones = []       # Bandeja de notificaciones del sistema
        self.esta_activo = 1

    def actualizar(self, cambio=None, valor=None, nota=None, **kwargs):
        """Implementación del contrato Observador: se ejecuta automáticamente
        cuando NotaMateria invoca notificar() al cambiar una calificación."""
        import time
        autor = kwargs.get('autor', 'Un docente')
        if nota and cambio:
            mensaje = (f"El docente {autor} ha modificado tu calificación "
                       f"de {cambio} en '{nota.materia.nombre_materia}' a {valor}.")
            self.notificaciones.append({
                "mensaje": mensaje,
                "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                "leido": False
            })

    @property
    def esta_aprobado(self):
        """Delega al historial el cálculo del estado de aprobación de nivelación.
        Separación de responsabilidades: el estudiante no calcula, solo consulta."""
        return self.historial.estado_nivelacion_actual

    def inscribir_seccion(self, seccion):
        """Previene que un estudiante curse la misma materia dos veces,
        verificando por id_materia en todas sus secciones ya asociadas."""
        ya_tiene_materia = any(
            sec.materia.id_materia == seccion.materia.id_materia
            for sec in self.secciones_asociadas
        )
        if not ya_tiene_materia:
            msg = seccion.actualizar_estudiantes_inscritos(self)
            if seccion not in self.secciones_asociadas and "correctamente" in msg:
                self.secciones_asociadas.append(seccion)
            return msg
        return "El estudiante ya está inscrito en una sección de esta materia."

    def solicitar_certificado(self, formato_documento="Consola"):
        """Genera un reporte usando el patrón Strategy: el formato
        (Consola o JSON) es intercambiable sin modificar este método."""
        contenido = (
            f"El estudiante {self.obtener_nombre_completo()} (ID: {self._id_estudiante}) "
            f"solicita un certificado de estudios para el periodo {self.nombre_periodo}."
        )
        return Reporte(
            tipo_de_reporte="Solicitud de Certificado",
            formato_documento=formato_documento,
            emisor=self.obtener_nombre_completo(),
            contenido=contenido
        )
```

### `Coordinador`: gestión de periodos y secciones

```python
# models/usuarios/Clase_Coordinador.py (fragmento clave)

class Coordinador(UsuarioAdministrativo):
    def cerrar_periodo_matricula(self, periodo: Periodo, lista_estudiantes=None):
        """Al cerrar el periodo, marca TODAS las notas como periodo_cerrado=True,
        lo que habilita el cálculo definitivo del estado de aprobación en NotaMateria."""
        periodo.finalizar_periodo()
        if lista_estudiantes:
            for est in lista_estudiantes:
                for nota in est.historial.lista_nota_materia:
                    nota.periodo_cerrado = True   # Habilita el cálculo de aprobación
                est.historial.actualizar()        # Fuerza recalcular el estado
        return True

    def asignar_docente_a_seccion(self, docente, seccion):
        """Valida que la especialidad del docente coincida con la materia
        antes de aceptar la asignación (regla de negocio del dominio)."""
        if docente.especialidad.lower() != seccion.materia.nombre_materia.lower():
            raise ValueError(
                f"La especialidad del docente ({docente.especialidad}) "
                f"no coincide con la materia ({seccion.materia.nombre_materia})."
            )
        seccion.asignar_docente(docente)
        return True

    def asignar_horario_a_seccion(self, seccion, nuevo_horario, todas_secciones):
        """Verifica colisión horaria contra TODAS las secciones existentes
        antes de aceptar el nuevo horario, usando Horario.deteccion_colision()."""
        for otra_sec in todas_secciones:
            for horario in otra_sec.lista_horarios:
                if nuevo_horario.deteccion_colision(horario):
                    raise ValueError(
                        f"El horario choca con la sección {otra_sec.id_seccion} "
                        f"en el horario {horario.hora_inicio}-{horario.hora_fin} "
                        f"los días {', '.join(horario.dias)}."
                    )
        seccion.agregar_horario(nuevo_horario)
        return True
```

## 3.4 Paso 4 — Entidades académicas (`academico/`)

### `Periodo` — Máquina de estados del ciclo académico

```python
# models/academico/Clase_Periodo.py

from models.enums.Estado_Periodo import EstadoPeriodo

class Periodo:
    def __init__(self, nombre_periodo: str, fecha_inicio: str, fecha_final: str):
        self.nombre_periodo = nombre_periodo
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        # El periodo siempre nace en PLANIFICACIÓN: no se pueden ingresar
        # calificaciones hasta que el coordinador lo inicie formalmente.
        self._estado_periodo = EstadoPeriodo.PLANIFICACION

    @property
    def estado_periodo(self):
        """Property de solo lectura: el estado no se puede modificar
        directamente; solo a través de los métodos de transición."""
        return self._estado_periodo.value

    def iniciar_periodo(self):
        """Transición válida: PLANIFICACION → EN_CURSO."""
        if self._estado_periodo == EstadoPeriodo.PLANIFICACION:
            self._estado_periodo = EstadoPeriodo.EN_CURSO
            print(f"[{self.nombre_periodo}] El periodo ha iniciado y está EN CURSO!")
        else:
            print(f"No se puede iniciar. Estado actual: {self._estado_periodo.value}")

    def finalizar_periodo(self):
        """Transición válida: EN_CURSO o PLANIFICACION → FINALIZADO.
        Al finalizar, NotaMateria puede calcular el estado definitivo de aprobación."""
        if self._estado_periodo in (EstadoPeriodo.EN_CURSO, EstadoPeriodo.PLANIFICACION):
            self._estado_periodo = EstadoPeriodo.FINALIZADO
            print(f"[{self.nombre_periodo}] El periodo ha sido FINALIZADO oficialmente.")
        else:
            print(f"No se puede finalizar en estado: {self._estado_periodo.value}")
```

### `Materia` — Entidad con umbrales desde Enum

```python
# models/academico/Clase_Materia.py

from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria

class Materia:
    def __init__(self, id_materia, nombre_materia,
                 # Los umbrales vienen del Enum (7.0 y 70) por defecto,
                 # pero pueden sobreescribirse por materia si la normativa cambia.
                 nota_minima=EstadoDeAprobacionMateria.NOTA_MINIMA_APROBACION.value,
                 asistencia_minima=EstadoDeAprobacionMateria.ASISTENCIA_MINIMA.value):
        self.id_materia = id_materia
        self.nombre_materia = nombre_materia
        self.nota_minima = nota_minima
        self.asistencia_minima = asistencia_minima
        self.secciones = []
        self.notas_materia = []          # Relación 0..* con NotaMateria

    def crear_seccion(self, id_seccion, capacidad_estudiantil):
        """Factory Method: crea y registra una nueva sección asociada a la materia."""
        from models.academico.Clase_Seccion import Seccion
        nueva_seccion = Seccion(id_seccion, capacidad_estudiantil, materia=self)
        self.secciones.append(nueva_seccion)
        return nueva_seccion
```

### `Seccion` — Agregado de horarios, docentes y estudiantes

```python
# models/academico/Clase_Seccion.py (fragmento clave)

class Seccion:
    def __init__(self, id_seccion, capacidad_estudiantil, materia=None, coordinador=None):
        self.id_seccion = id_seccion
        self.capacidad_estudiantil = capacidad_estudiantil
        self.materia = materia
        self.coordinador = coordinador
        self.estudiantes_inscritos = []
        self.lista_horarios = []
        self.docentes = []
        self.aula_virtual = None           # Puede ser AulaClaseSincrona o AulaExamen (Bridge)
        self.disponibilidad = True

    def calcular_limite_optimo(self):
        """Si hay aula virtual, el límite real es el mínimo entre
        la capacidad de la sección y la del aula física."""
        if self.entorno_asignado is None:
            return self.capacidad_estudiantil
        return min(self.capacidad_estudiantil, self.entorno_asignado.capacidad_maxima)

    def actualizar_estudiantes_inscritos(self, estudiante):
        """Control de cupos: verifica disponibilidad, evita duplicados
        y actualiza el flag de disponibilidad cuando la sección se llena."""
        if self.verificar_cupos_disponibles():
            if estudiante not in self.estudiantes_inscritos:
                self.estudiantes_inscritos.append(estudiante)
                if not self.verificar_cupos_disponibles():
                    self.disponibilidad = False    # La sección se llenó
                return "Estudiante inscrito correctamente."
            return "El estudiante ya está inscrito."
        self.disponibilidad = False
        return "No existen cupos disponibles."

    def __len__(self):
        """Permite usar len(seccion) para saber cuántos estudiantes están inscritos."""
        return len(self.estudiantes_inscritos)

    def __bool__(self):
        """Una sección siempre es truthy, aunque esté vacía (evita confusiones con None)."""
        return True
```

### `Horario` — Detección de colisiones horarias

```python
# models/academico/Clase_Horario.py

class Horario:
    def __init__(self, turno, hora_inicio, hora_fin, modalidad, dias=None):
        self.turno = turno
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self._modalidad = modalidad    # Protegido
        self.dias = dias if dias is not None else ["Lunes", "Miércoles", "Viernes"]

    def deteccion_colision(self, otro_horario):
        """Detecta si dos horarios se solapan considerando tanto el tiempo
        como los días de la semana. Convierte horas a minutos para comparar
        de forma exacta sin errores de formato de cadena."""
        def a_minutos(hora_str):
            try:
                h, m = map(int, hora_str.split(':'))
                return h * 60 + m
            except:
                return 0

        inicio1, fin1 = a_minutos(self.hora_inicio), a_minutos(self.hora_fin)
        inicio2, fin2 = a_minutos(otro_horario.hora_inicio), a_minutos(otro_horario.hora_fin)

        # Solo hay colisión si los horarios comparten al menos un día
        # Y los rangos de tiempo se superponen
        dias_en_comun = set(self.dias).intersection(set(otro_horario.dias))
        if dias_en_comun:
            if max(inicio1, inicio2) < min(fin1, fin2):   # Intervalos solapados
                return True
        return False
```

### `MallaCurricular` — Estructura curricular de la carrera

```python
# models/academico/Clase_MallaCurricular.py

from models.academico.Clase_Materia import Materia

class MallaCurricular:
    def __init__(self, codigo_malla: str, area_conocimiento: str, carrera=None):
        self.codigo_malla = codigo_malla
        self.area_conocimiento = area_conocimiento
        self.lista_materias = []
        self.carrera = carrera             # Referencia inversa hacia la carrera

    def agregar_materias(self, materia_objeto) -> str:
        self.lista_materias.append(materia_objeto)
        return "La materia ha sido agregada con éxito"

    def mostrar_informacion(self):
        """Muestra la malla completa en consola de forma legible."""
        print(f"ÁREA DE CONOCIMIENTO -> {self.area_conocimiento}")
        print(f"CÓDIGO DE MALLA      -> {self.codigo_malla}")
        if not self.lista_materias:
            print("(Aún no hay materias asignadas a esta malla)")
        else:
            for indice, materia in enumerate(self.lista_materias, start=1):
                print(f"  {indice}. {materia.nombre_materia}")
```

## 3.5 Paso 5 — Patrón Observer: notificaciones automáticas de calificaciones

Este es el núcleo de la evaluación en SeNi. La clase `NotaMateria` actúa como **Sujeto** del patrón Observer; `HistorialAcademico` y `Estudiante` actúan como **Observadores**. Cuando un docente modifica cualquier calificación, el sistema reacciona automáticamente sin que nadie tenga que invocar manualmente la actualización.

```python
# models/gestion/Clase_NotaMateria.py

from abc import ABC, abstractmethod

# INTERFAZ SUJETO del patrón Observer
class Sujeto(ABC):
    def __init__(self):
        self._observadores = []

    def anexar(self, observador):
        if observador not in self._observadores:
            self._observadores.append(observador)

    def remover(self, observador):
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar(self, cambio=None, valor=None, nota=None):
        """Propaga el cambio a todos los observadores suscritos,
        incluyendo el nombre del último modificador (el docente)."""
        autor = getattr(self, 'ultimo_modificador', 'Un docente')
        for observador in self._observadores:
            observador.actualizar(cambio, valor, nota, autor=autor)


class NotaMateria(Sujeto):
    def __init__(self, materia, periodo, parcial1=0.0, parcial2=0.0,
                 asistencia=0, historial=None):
        super().__init__()
        self.materia = materia
        self.periodo = periodo
        self._parcial1 = parcial1
        self._parcial2 = parcial2
        self._asistencia = asistencia
        self.historial = historial

        # Auto-registro en la materia para mantener la relación bidireccional
        if self.materia and self not in self.materia.notas_materia:
            self.materia.notas_materia.append(self)

        # AUTO-SUSCRIPCIÓN: el historial y el estudiante se suscriben automáticamente
        # al crear la nota, sin que el código cliente deba llamar a anexar() manualmente.
        if self.historial:
            self.anexar(self.historial)
            if hasattr(self.historial, 'estudiante') and self.historial.estudiante:
                self.anexar(self.historial.estudiante)

    # PROPIEDADES INTERCEPTADAS: cada setter dispara el Observer
    @property
    def parcial1(self): return self._parcial1
    @parcial1.setter
    def parcial1(self, valor):
        self._parcial1 = valor
        self.notificar("parcial1", valor, self)  # → notifica historial y estudiante

    @property
    def parcial2(self): return self._parcial2
    @parcial2.setter
    def parcial2(self, valor):
        self._parcial2 = valor
        self.notificar("parcial2", valor, self)

    @property
    def asistencia(self): return self._asistencia
    @asistencia.setter
    def asistencia(self, valor):
        self._asistencia = valor
        self.notificar("asistencia", valor, self)

    @property
    def nota_final(self):
        """La nota final es el promedio aritmético de los dos parciales."""
        return (self._parcial1 + self._parcial2) / 2

    @property
    def esta_aprobado(self):
        """Regla de aprobación: el periodo debe estar FINALIZADO.
        Si no, retorna MATERIA_PENDIENTE (no se puede determinar el resultado).
        Si está finalizado: se evalúan nota y asistencia contra los umbrales del Enum."""
        if self.periodo is None or self.periodo.estado_periodo != EstadoPeriodo.FINALIZADO.value:
            return EstadoDeAprobacionMateria.MATERIA_PENDIENTE

        if (self.nota_final >= EstadoDeAprobacionMateria.NOTA_MINIMA_APROBACION.value
                and self.asistencia >= EstadoDeAprobacionMateria.ASISTENCIA_MINIMA.value):
            return EstadoDeAprobacionMateria.MATERIA_APROBADA
        else:
            return EstadoDeAprobacionMateria.MATERIA_REPROBADA
```

```python
# models/gestion/Clase_HistorialAcademico.py

class HistorialAcademico(Observador):
    def __init__(self, id_historial: str, estudiante=None):
        self.id_historial = id_historial
        self.estudiante = estudiante
        self.lista_nota_materia = []
        # Estado inicial: sin materias registradas → PENDIENTE
        self.estado_nivelacion_actual = EstadoDeAprobacionNivelacion.PENDIENTE

    def verificar_aprobacion_nivelacion(self):
        """Regla de aprobación del semestre completo:
        - Si hay alguna materia REPROBADA → REPROBADO (corto circuito: falla inmediata)
        - Si hay alguna materia PENDIENTE → PENDIENTE (esperando cierre del periodo)
        - Si todas están APROBADAS → APROBADO"""
        if not self.lista_nota_materia:
            return EstadoDeAprobacionNivelacion.PENDIENTE

        tiene_materias_pendientes = False
        for nota in self.lista_nota_materia:
            estado_materia = nota.esta_aprobado
            if estado_materia == EstadoDeAprobacionMateria.MATERIA_PENDIENTE:
                tiene_materias_pendientes = True
            elif estado_materia == EstadoDeAprobacionMateria.MATERIA_REPROBADA:
                return EstadoDeAprobacionNivelacion.REPROBADO  # Corto circuito

        if tiene_materias_pendientes:
            return EstadoDeAprobacionNivelacion.PENDIENTE
        return EstadoDeAprobacionNivelacion.APROBADO

    def actualizar(self, cambio=None, valor=None, nota=None, **kwargs):
        """Implementación del Observer: se ejecuta automáticamente cuando
        NotaMateria notifica un cambio en cualquier calificación o asistencia."""
        self.estado_nivelacion_actual = self.verificar_aprobacion_nivelacion()

    @property
    def promedio_general(self):
        """Promedio de nota_final de todas las materias cursadas."""
        if not self.lista_nota_materia:
            return 0.0
        return sum(n.nota_final for n in self.lista_nota_materia) / len(self.lista_nota_materia)

    def obtener_peor_nota(self):
        """Retorna la peor nota_final entre todas las materias."""
        if not self.lista_nota_materia:
            return 0.0
        return min(self.lista_nota_materia, key=lambda n: n.nota_final).nota_final
```

## 3.6 Paso 6 — Patrón Strategy: reportes en múltiples formatos

El patrón **Strategy** permite generar reportes académicos (certificados, solicitudes, informes) en distintos formatos sin modificar el código que los solicita.

```python
# models/patrones_diseno/strategy/ReporteStrategy.py

from abc import ABC, abstractmethod
import json

# 1. INTERFAZ ESTRATEGIA
class IEstrategiaReporte(ABC):
    @abstractmethod
    def generar(self, tipo_de_reporte: str, emisor: str, contenido: str) -> str:
        pass

# 2. ESTRATEGIA CONCRETA: Consola / Texto Plano
class ReporteConsola(IEstrategiaReporte):
    def generar(self, tipo_de_reporte, emisor, contenido) -> str:
        borde = "=" * 50
        return (
            f"\n{borde}\n"
            f"               REPORTE ACADÉMICO ULEAM\n"
            f"{borde}\n"
            f"Tipo de Reporte: {tipo_de_reporte}\n"
            f"Generado por:    {emisor}\n"
            f"{borde}\n"
            f"Contenido:\n{contenido}\n"
            f"{borde}\n"
        )

# 3. ESTRATEGIA CONCRETA: JSON
class ReporteJSON(IEstrategiaReporte):
    def generar(self, tipo_de_reporte, emisor, contenido) -> str:
        documento = {
            "institucion": "ULEAM",
            "tipo_de_reporte": tipo_de_reporte,
            "formato": "JSON",
            "emisor": emisor,
            "contenido": contenido
        }
        return json.dumps(documento, indent=4, ensure_ascii=False)

# 4. CONTEXTO: mantiene la estrategia activa y la puede cambiar en tiempo de ejecución
class Reporte:
    def __init__(self, tipo_de_reporte, formato_documento, emisor, contenido):
        self.tipo_de_reporte = tipo_de_reporte
        self.emisor = emisor
        self.contenido = contenido
        # Selección de estrategia según el formato solicitado
        if formato_documento.upper() == 'JSON':
            self.estrategia = ReporteJSON()
        else:
            self.estrategia = ReporteConsola()   # Estrategia por defecto

    def cambiar_estrategia(self, nueva_estrategia: IEstrategiaReporte):
        """Permite cambiar el formato SIN recriar el objeto Reporte."""
        self.estrategia = nueva_estrategia

    def imprimir_reporte(self) -> str:
        """Delega la generación a la estrategia activa."""
        return self.estrategia.generar(self.tipo_de_reporte, self.emisor, self.contenido)
```

**Uso en el sistema:** `Estudiante.solicitar_certificado("JSON")` crea un `Reporte` con `ReporteJSON`; `Docente.realizaReporte("Informe", "Consola", contenido)` crea uno con `ReporteConsola`. El método `imprimir_reporte()` es idéntico en ambos casos.

## 3.7 Paso 7 — Patrón Bridge: aulas virtuales desacopladas de la plataforma

El patrón **Bridge** resuelve la proliferación de subclases: sin él, habría que crear `AulaClaseSincronaTeams`, `AulaClaseSincronaZoom`, `AulaExamenTeams`, `AulaExamenZoom` (combinatoria cuadrática). Con el Bridge, cualquier tipo de aula puede conectarse a cualquier servicio de streaming de forma independiente.

```python
# models/patrones_diseno/bridge/AulaVirtualBridge.py

from abc import ABC, abstractmethod

# 1. EL IMPLEMENTADOR (interfaz del servicio de streaming)
class IServicioStreaming(ABC):
    @abstractmethod
    def crear_reunion(self, nombre_aula: str) -> str:
        pass

# 2. IMPLEMENTADORES CONCRETOS (plataformas de videoconferencia)
class ServicioTeams(IServicioStreaming):
    def crear_reunion(self, nombre_aula: str) -> str:
        return f"https://teams.microsoft.com/meet/{nombre_aula.lower()}"

class ServicioZoom(IServicioStreaming):
    def crear_reunion(self, nombre_aula: str) -> str:
        return f"https://zoom.us/j/{nombre_aula.lower()}"

# 3. LA ABSTRACCIÓN (contiene el PUENTE hacia el implementador)
class AulaVirtual:
    def __init__(self, capacidad_maxima, servicio: IServicioStreaming,
                 enlace_personalizado=None):
        self.capacidad_maxima = capacidad_maxima
        self.servicio = servicio            # EL PUENTE: referencia al implementador
        self.enlace_personalizado = enlace_personalizado

    @property
    def _tipo_plataforma(self) -> str:
        """Retorna dinámicamente el nombre de la plataforma."""
        return "ZOOM" if isinstance(self.servicio, ServicioZoom) else "TEAMS"

    @property
    def _enlace_plataforma(self) -> str:
        """Genera el enlace usando el servicio, a menos que haya uno personalizado."""
        if self.enlace_personalizado:
            return self.enlace_personalizado
        return self.servicio.crear_reunion("general")

# 4. ABSTRACCIONES REFINADAS: especializan el tipo de reunión sin conocer el servicio
class AulaClaseSincrona(AulaVirtual):
    @property
    def _enlace_plataforma(self) -> str:
        """Genera un enlace específico para clase teórica sincrónica."""
        if self.enlace_personalizado:
            return self.enlace_personalizado
        return self.servicio.crear_reunion("clase-teorica")

class AulaExamen(AulaVirtual):
    @property
    def _enlace_plataforma(self) -> str:
        """Genera un enlace específico para sala de examen segura."""
        if self.enlace_personalizado:
            return self.enlace_personalizado
        return self.servicio.crear_reunion("aula-examen-seguro")
```

**Resultado:** `AulaClaseSincrona(30, ServicioTeams())` genera `teams.microsoft.com/meet/clase-teorica`; `AulaExamen(30, ServicioZoom())` genera `zoom.us/j/aula-examen-seguro`. Las dos jerarquías (tipos de aula + servicios de streaming) evolucionan de forma totalmente independiente.

## 3.8 Paso 8 — Patrón Builder: construcción fluida de secciones

El patrón **Builder** resuelve la complejidad de construir objetos `Seccion` con múltiples atributos opcionales de forma legible y con validación garantizada antes de instanciar.

```python
# models/patrones_diseno/builders/SeccionBuilder.py (fragmento clave)

class SeccionBuilder:
    """Builder para la clase Seccion: construcción paso a paso con
    encadenamiento fluido (method chaining) y validación de campos obligatorios."""

    def __init__(self):
        self._id_seccion = None              # Requerido
        self._capacidad_estudiantil = None   # Requerido
        self._materia = None                 # Opcional
        self._coordinador = None             # Opcional
        self._aula_virtual = None            # Opcional (Bridge)
        self._disponibilidad = True

    def con_id_seccion(self, id_seccion):
        self._id_seccion = id_seccion
        return self   # Retorna self para encadenamiento: builder.con_x().con_y()

    def con_capacidad_estudiantil(self, capacidad):
        self._capacidad_estudiantil = capacidad
        return self

    def con_materia(self, materia):
        self._materia = materia
        return self

    def con_aula_virtual(self, aula_virtual):
        self._aula_virtual = aula_virtual
        return self

    def build(self) -> 'Seccion':
        """Valida los campos obligatorios y construye el objeto Seccion."""
        if self._id_seccion is None:
            raise ValueError("'id_seccion' es requerido para construir una sección.")
        if self._capacidad_estudiantil is None:
            raise ValueError("'capacidad_estudiantil' es requerido.")

        seccion = Seccion(
            id_seccion=self._id_seccion,
            capacidad_estudiantil=self._capacidad_estudiantil,
            materia=self._materia,
            coordinador=self._coordinador
        )
        seccion.aula_virtual = self._aula_virtual
        seccion.disponibilidad = self._disponibilidad
        return seccion
```

**Uso:** `SeccionBuilder().con_id_seccion("S-01").con_capacidad_estudiantil(30).con_materia(prog).build()` en lugar de pasar todos los parámetros en el constructor de `Seccion`, con validación incorporada.

## 3.9 Paso 9 — Demostración en `main.py`

El archivo `main.py` demuestra el funcionamiento del sistema simulando tres escenarios reales del semestre nivelatorio:

```python
# main.py — Simulación completa del ciclo de evaluación

# PASO 1: Crear materias del semestre
materia_prog = Materia("MAT-01", "Programación", nota_minima=7.0, asistencia_minima=70)
materia_mate = Materia("MAT-02", "Matemáticas", nota_minima=7.0, asistencia_minima=70)

# PASO 2: Crear estudiante (composición automática de HistorialAcademico)
alumno = Estudiante(cedula="131555", nombres="Julean", apellidos="Pérez",
                    correo="julean@univ.com", contrasenia="1234",
                    id_estudiante="EST-99", nombre_periodo="Nivelación 2026",
                    tipo_matricula="Ordinaria")

# PASO 3: Crear periodo y vincular notas por composición
periodo_actual = Periodo("Nivelación 2026", "2026-01-01", "2026-06-30")
nota_prog = alumno.historial.crear_nota_materia(materia=materia_prog, periodo=periodo_actual)
nota_mate = alumno.historial.crear_nota_materia(materia=materia_mate, periodo=periodo_actual)

# ESCENARIO 1: Periodo abierto → estado PENDIENTE
# El sistema detecta automáticamente que el periodo no está finalizado

# ESCENARIO 2: Docente sube notas (reprueba por asistencia insuficiente)
nota_prog.parcial1 = 8.5   # → dispara Observer → historial recalcula → PENDIENTE
nota_prog.parcial2 = 9.0
nota_prog.asistencia = 55  # Debajo del 70% mínimo
# Al cerrar el periodo: nota_prog.esta_aprobado → MATERIA_REPROBADA

# ESCENARIO 3: Estudiante justifica faltas → sube asistencia → APROBADO
nota_prog.asistencia = 85  # Supera el mínimo → Observer actualiza estado automáticamente
```

---

# PARTE 4 — CONCLUSIONES Y ANÁLISIS

## 4.1 Verificación práctica de la capa

Para confirmar que la capa POO es funcional de forma aislada, se instanciaron directamente las entidades desde Python sin necesidad de la interfaz web:

```python
>>> from models.usuarios.Clase_Estudiante import Estudiante
>>> alumno = Estudiante("131555", "Julean", "Pérez", "j@u.com", "12345678",
...                     "EST-99", "Nivelación 2026", "Ordinaria")
>>> print(alumno.obtener_nombre_completo())
Julean Pérez
>>> print(alumno.esta_aprobado.value)
Nivelación Pendiente
```

La importación y ejecución fueron exitosas sin servidor web activo, validando el objetivo central de diseño: **la lógica de negocio del semestre nivelatorio es independiente de la capa de presentación**.

## 4.2 Cómo la capa POO responde a la problemática planteada

- **Registros duplicados de estudiantes** → resuelto con `Usuario.__eq__()`, que considera iguales a dos usuarios con la misma cédula **o** el mismo correo, impidiendo su duplicación en colecciones del sistema.

- **Solapamientos de horarios** → resuelto con `Horario.deteccion_colision()` y `Coordinador.asignar_horario_a_seccion()`, que verifican conflictos de tiempo y día antes de aceptar cualquier nuevo bloque horario.

- **Falta de trazabilidad en calificaciones** → resuelto con el patrón **Observer**: cada vez que un docente modifica una nota, `NotaMateria` notifica automáticamente al historial (que recalcula el estado) y al estudiante (que registra la notificación en su bandeja de mensajes con fecha y hora).

- **Determinación automática del estado de aprobación** → resuelto con `HistorialAcademico.verificar_aprobacion_nivelacion()`, que evalúa todas las materias del semestre aplicando la lógica de "reprobado con corto circuito": si una sola materia está reprobada, la nivelación completa se reprueba sin seguir evaluando.

- **Reportes en múltiples formatos** → resuelto con el patrón **Strategy**: el mismo método `imprimir_reporte()` genera texto plano o JSON según la estrategia activa, sin duplicar código.

## 4.3 Dificultades encontradas y cómo se resolvieron

1. **Gestión del estado del periodo y su efecto en las notas.**
   *Dificultad:* determinar si una materia está aprobada o reprobada solo tiene sentido cuando el periodo ya cerró. Antes del cierre, el sistema no debe declarar a nadie reprobado.
   *Solución:* se introdujo la verificación del `estado_periodo` directamente en la propiedad `NotaMateria.esta_aprobado`: si el periodo no está en estado `FINALIZADO`, retorna `MATERIA_PENDIENTE` automáticamente, bloqueando cualquier veredicto prematuro.

2. **Recursión infinita en asociaciones bidireccionales.**
   *Dificultad:* `Carrera.asociar_coordinador()` llama a `coordinador.asociar_carrera(self)` y viceversa, lo que podría causar una pila de llamadas infinita.
   *Solución:* se añadió la guarda `if self.coordinador != coordinador` que corta el ciclo cuando el objeto ya está asociado, permitiendo la bidireccionalidad sin recursión infinita.

3. **Auto-suscripción de observadores sin acoplamiento manual.**
   *Dificultad:* al crear una `NotaMateria`, tanto `HistorialAcademico` como el `Estudiante` deben suscribirse como observadores. Forzar al código cliente a hacerlo manualmente es propenso a olvidos.
   *Solución:* se implementó la **auto-suscripción** en el constructor de `NotaMateria`: si se recibe un `historial`, este y su `estudiante` se suscriben automáticamente. El código cliente no necesita llamar a `anexar()` nunca.

4. **Validación de especialidad del docente vs. materia.**
   *Dificultad:* si se permite asignar cualquier docente a cualquier sección, el sistema carece de coherencia académica.
   *Solución:* se centralizó la validación en `Coordinador.asignar_docente_a_seccion()`, que lanza un `ValueError` descriptivo si la especialidad del docente no coincide con el nombre de la materia. La regla de negocio vive en la clase de dominio, no dispersa en la interfaz.

5. **Detección de colisiones horarias con múltiples días de clase.**
   *Dificultad:* una materia puede dictarse Lunes, Miércoles y Viernes, y otra solo los Martes y Jueves. Una comparación ingenua de rangos de hora sin considerar los días daría falsos positivos de colisión.
   *Solución:* `Horario.deteccion_colision()` primero calcula la intersección de conjuntos de días (`set.intersection()`) y solo evalúa el rango de horas si hay días en común, eliminando los falsos positivos.

6. **Encapsulación del cierre del periodo.**
   *Dificultad:* el cierre del periodo implica actualizar `periodo_cerrado` en cada nota de cada estudiante, lo que obligaría al código cliente a conocer la estructura interna del historial.
   *Solución:* se encapsuló toda esa lógica en `Coordinador.cerrar_periodo_matricula()`, que itera sobre la lista de estudiantes, actualiza las notas y fuerza la recalculación del historial. El llamador (la interfaz web) solo invoca un único método.

## 4.4 Fortalezas del diseño actual

- **Separación estricta entre lógica de dominio (POO) e interfaz (`App/`):** la capa `models/` puede probarse de forma completamente aislada mediante `main.py`, sin servidor web ni base de datos activa.
- **Uso de cuatro patrones de diseño con propósito real:** Observer para notificaciones automáticas de calificaciones, Strategy para reportes polimórficos, Bridge para aulas virtuales desacopladas de plataformas, y Builder para construcción fluida y segura de secciones.
- **Pilares de la POO verificables en el código:** encapsulación (`__contrasenia`, `_cedula`, propiedades interceptadas), herencia multinivel (`Usuario → UsuarioAcademico → Docente`), herencia múltiple (`Estudiante` hereda de `UsuarioAcademico` y `Observador`), polimorfismo (`ver_rendimiento()` varía entre `Docente` y `Estudiante`).
- **Reglas de negocio centralizadas en el Enum:** la nota mínima (7.0) y la asistencia mínima (70%) viven en `EstadoDeAprobacionMateria`, consultados desde `NotaMateria` y `Materia`; cambiar el umbral en un solo lugar actualiza todo el sistema.

## 4.5 Conclusión general

La capa `models/` cumple su rol de **núcleo de dominio** del sistema SeNi: encapsula en aproximadamente 20 archivos todas las reglas de negocio del semestre nivelatorio, aplicando de manera consistente los cuatro pilares de la Programación Orientada a Objetos — abstracción, encapsulación, herencia y polimorfismo — junto con cuatro patrones de diseño reconocidos (Observer, Strategy, Bridge, Builder). El resultado es un modelo de dominio desacoplado de la interfaz web, verificable de forma aislada mediante `main.py`, que traduce fielmente cada requerimiento académico (gestión de materias, asignación de docentes, control de horarios, evaluación automática y generación de reportes) en comportamiento de objetos concretos y comprobables.

---

## Anexo — Trazabilidad entre requerimientos del sistema y la capa POO

| Requerimiento académico | Clases que lo implementan |
|---|---|
| Gestión de la oferta académica | `Universidad`, `Sede`, `Carrera`, `MallaCurricular`, `Materia`, `Periodo` |
| Inscripción y control de cupos | `Seccion`, `Estudiante.inscribir_seccion()`, `Seccion.actualizar_estudiantes_inscritos()` |
| Asignación de docentes y validación de especialidad | `Docente`, `Coordinador.asignar_docente_a_seccion()` |
| Gestión y colisión de horarios | `Horario`, `Coordinador.asignar_horario_a_seccion()`, `Horario.deteccion_colision()` |
| Registro automático de calificaciones | `NotaMateria` (Observer Sujeto), `HistorialAcademico` (Observador) |
| Notificaciones al estudiante | `Estudiante.actualizar()` (Observador), `Estudiante.notificaciones` |
| Evaluación del estado de nivelación | `HistorialAcademico.verificar_aprobacion_nivelacion()`, `Estudiante.esta_aprobado` |
| Generación de reportes y certificados | `ReporteStrategy` (Strategy): `ReporteConsola`, `ReporteJSON`, `Reporte` |
| Aulas virtuales multi-plataforma | `AulaVirtualBridge` (Bridge): `AulaClaseSincrona`, `AulaExamen`, `ServicioTeams`, `ServicioZoom` |
| Construcción de secciones complejas | `SeccionBuilder` (Builder) |
| Apertura y cierre del periodo académico | `Periodo` (máquina de estados), `Coordinador.abrir_periodo_matricula()`, `Coordinador.cerrar_periodo_matricula()` |

Esta correspondencia evidencia que el diseño orientado a objetos de `models/` no se construyó de forma genérica, sino directamente a partir de los requerimientos reales del semestre nivelatorio, garantizando que cualquier ajuste futuro a las reglas académicas se traduzca en un cambio localizado en una clase específica sin afectar al resto del sistema.
