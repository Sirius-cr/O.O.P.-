dependiendo de la cantidad de estudiantes ingresados en una carrera por el coordinador al momento de crear una materia, se crearán secciones dividiendo los estudiantes segun la capacidadEstudiantil de cada seccion, la cantidad de estudiantes que el coordinador pueda ingresar debe ser par, y poder dividirse de manera uniforme en varias secciones (100 / 4 = 4 secciones de 25 estudiantes)

seccion se haria con un builder, y quedaria en None el docenteAsignado, el entornoAsignado, la listaHorarios, estudiantesInscritos.

crearEntornoAcademico(), lo que hara sera recibir un objeto de tipo EntornoAcademico, es decir será una inyeccion de dependencias.

El reporte de los docentes sera un cuadro de texto, donde aparecera la fecha y permita subir archivos
El reporte de los estudiantes será cuando llamen al metodo solicitarRetiro(), solo será completar un formulario, tambien registrará la fecha automaticamente.

2 metodos de coordinador se realizarán una vez que se programe correctamente horario y seccion.

verHorario() metodo de los usuariosAcademicos se programará una vez que se termine correctamente seccion y horario.

La clase NotaMateria aun no implemente al completo la logica porque aun no se finaliza la codificacion de la clase Periodo

Realizar pruebas de feature 2 una vez que se termine de programar el nuevo UML

Crear interfaz grafica
Agregar un patron estructural al sistema

27-06-2026
-Revisar el archivo AulaVirtual.py para ver comprobar si funcionan todos sus metodos

-En la clase horario no se entiende bien la validación de deteccion de colision, y en resumen_de_seccion, existe un metodo que no esta implementado

-Modificar malla curricular y carrera, dentro de carrera debe existir un atributo llamado malla curricular, el cual termina creando un objeto de malla curricular y lo almacena

-Materia esta bien

-Periodo: Revisar los metodos que tengan algo relacionado con oferta academica, ya que esa clase hay que eliminarla, revisar metodo cambiar_estado, ya que existen otros metodos que parecen hacer lo mismo