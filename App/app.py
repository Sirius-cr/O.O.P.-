import sys
import os
import webbrowser
import threading
import time
import json
from flask import Flask, render_template, request, jsonify, redirect, url_for, session

# Añadir el directorio raíz al path para poder importar las clases de models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.usuarios.Clase_Estudiante import Estudiante
from models.usuarios.Clase_Docente import Docente
from models.usuarios.Clase_Coordinador import Coordinador
from models.academico.Clase_Materia import Materia
from models.academico.Clase_Seccion import Seccion
from models.academico.Clase_Periodo import Periodo
from models.academico.Clase_Horario import Horario
from models.patrones_diseno.bridge.AulaVirtualBridge import AulaVirtual, AulaClaseSincrona, AulaExamen, ServicioTeams, ServicioZoom
from models.enums.Estado_Aprobacion import EstadoDeAprobacionMateria, EstadoDeAprobacionNivelacion
from models.institucion.Clase_Carrera import Carrera
from models.patrones_diseno.strategy.ReporteStrategy import Reporte
from models.gestion.Clase_NotaMateria import NotaMateria
from models.patrones_diseno.builders.SeccionBuilder import SeccionBuilder

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_webview_app'

# Ruta absoluta al archivo JSON
DB_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database', 'db.json'))

# =========================================================================
# VARIABLES GLOBALES DE INSTANCIAS POO
# =========================================================================
periodo_actual = None
materias = {}
carrera_software = None
estudiantes = {}
docentes = {}
coordinadores = {}
secciones = {}
solicitudes_retiro = []
reportes_generados = []

# =========================================================================
# CARGA Y GUARDADO DE LA BASE DE DATOS JSON A OBJETOS POO
# =========================================================================
def load_db():
    global periodo_actual, materias, carrera_software, estudiantes, docentes, coordinadores, secciones, solicitudes_retiro, reportes_generados
    
    if not os.path.exists(DB_FILE):
        raise FileNotFoundError(f"No se encontró el archivo de base de datos en: {DB_FILE}")
        
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # 1. Cargar Período Académico
    p_data = data["periodo"]
    periodo_actual = Periodo(
        nombre_periodo=p_data["nombre_periodo"],
        fecha_inicio=p_data["fecha_inicio"],
        fecha_final=p_data["fecha_final"]
    )
    from models.enums.Estado_Periodo import EstadoPeriodo
    for state_enum in EstadoPeriodo:
        if state_enum.value == p_data["estado_periodo"]:
            periodo_actual._estado_periodo = state_enum
            break

    # 2. Cargar Materias
    materias = {}
    for m in data["materias"]:
        materias[m["id_materia"]] = Materia(
            id_materia=m["id_materia"],
            nombre_materia=m["nombre_materia"],
            nota_minima=m["nota_minima"],
            asistencia_minima=m["asistencia_minima"]
        )

    # 3. Cargar Carreras
    c_data = data["carreras"][0]
    carrera_software = Carrera(
        id_carrera=c_data["id_carrera"],
        nombre_carrera=c_data["nombre_carrera"],
        capacidad_estudiantil=c_data["capacidad_estudiantil"]
    )

    # 4. Cargar Coordinadores
    coordinadores = {}
    for c in data["usuarios"]["coordinadores"]:
        coord = Coordinador(
            cedula=c["cedula"],
            nombres=c["nombres"],
            apellidos=c["apellidos"],
            correo=c["correo"],
            contrasenia=c["contrasenia"],
            id_coordinador=c["id_coordinador"],
            fecha_asignacion_cargo=c["fecha_asignacion_cargo"]
        )
        coord.asociar_carrera(carrera_software)
        coordinadores[coord._correo] = coord

    # 5. Cargar Docentes
    docentes = {}
    for d in data["usuarios"]["docentes"]:
        doc = Docente(
            cedula=d["cedula"],
            nombres=d["nombres"],
            apellidos=d["apellidos"],
            correo=d["correo"],
            contrasenia=d["contrasenia"],
            especialidad=d["especialidad"]
        )
        docentes[doc._correo] = doc

    # 6. Cargar Estudiantes
    estudiantes = {}
    for e in data["usuarios"]["estudiantes"]:
        est = Estudiante(
            cedula=e["cedula"],
            nombres=e["nombres"],
            apellidos=e["apellidos"],
            correo=e["correo"],
            contrasenia=e["contrasenia"],
            id_estudiante=e["id_estudiante"],
            nombre_periodo=e["nombre_periodo"],
            tipo_matricula=e["tipo_matricula"]
        )
        estudiantes[est._correo] = est

    # 7. Cargar Secciones
    secciones = {}
    for s in data["secciones"]:
        m_obj = materias.get(s["materia_id"])
        coord_obj = list(coordinadores.values())[0] if coordinadores else None
        
        sec = (SeccionBuilder()
               .con_id_seccion(s["id_seccion"])
               .con_capacidad_estudiantil(s["capacidad_estudiantil"])
               .con_materia(m_obj)
               .con_coordinador(coord_obj)
               .build())
        
        # Asignar Docentes
        for doc_email in s["docentes_correos"]:
            doc_obj = docentes.get(doc_email)
            if doc_obj:
                sec.asignar_docente(doc_obj)
                
        # Asignar Horarios
        for h in s["horarios"]:
            sec.agregar_horario(Horario(h["turno"], h["hora_inicio"], h["hora_fin"], h["modalidad"]))
            
        # Asignar Aula Virtual
        if s["aula_virtual"]:
            av = s["aula_virtual"]
            if av["tipo_plataforma"].upper() == "ZOOM":
                servicio = ServicioZoom()
            else:
                servicio = ServicioTeams()
            
            # Instanciar la abstracción refinada apropiada
            is_examen = "examen" in s.get("materia_id", "").lower()
            if is_examen:
                aula = AulaExamen(av["capacidad_maxima"], servicio)
            else:
                aula = AulaClaseSincrona(av["capacidad_maxima"], servicio)
                
            sec.asignar_aula_virtual(aula)
            
        # Inscribir Estudiantes
        for est_id in s["estudiantes_ids"]:
            est_obj = next((e for e in estudiantes.values() if e._id_estudiante == est_id), None)
            if est_obj:
                est_obj.inscribir_seccion(sec)
                
        secciones[sec.id_seccion] = sec

    # 8. Cargar Notas
    for n in data.get("notas", []):
        est_obj = next((e for e in estudiantes.values() if e._id_estudiante == n["estudiante_id"]), None)
        m_obj = materias.get(n["materia_id"])
        if est_obj and m_obj:
            nota_obj = next((x for x in est_obj.historial.lista_nota_materia if x.materia.id_materia == m_obj.id_materia), None)
            if not nota_obj:
                nota_obj = est_obj.historial.crear_nota_materia(
                    materia=m_obj,
                    periodo=periodo_actual,
                    parcial1=n["parcial1"],
                    parcial2=n["parcial2"],
                    asistencia=n["asistencia"]
                )
            else:
                nota_obj.parcial1 = n["parcial1"]
                nota_obj.parcial2 = n["parcial2"]
                nota_obj.asistencia = n["asistencia"]
            nota_obj.periodo_cerrado = n["periodo_cerrado"]

    # 9. Cargar Solicitudes de Retiro
    solicitudes_retiro = []
    for sol in data.get("solicitudes_retiro", []):
        est_obj = next((e for e in estudiantes.values() if e._id_estudiante == sol["estudiante_id"]), None)
        reporte = None
        if est_obj:
            reporte = Reporte("Solicitud de Retiro", "Consola", est_obj.obtener_nombre_completo(), sol["motivo"])
            
        solicitudes_retiro.append({
            "id": sol["id"],
            "estudiante_id": sol["estudiante_id"],
            "nombre": sol["nombre"],
            "correo": sol["correo"],
            "motivo": sol["motivo"],
            "fecha": sol["fecha"],
            "estado": sol["estado"],
            "reporte": reporte
        })

    # 10. Cargar Reportes Generados
    reportes_generados = []
    for r in data.get("reportes_generados", []):
        reportes_generados.append(Reporte(
            tipo_de_reporte=r["tipo_de_reporte"],
            formato_documento=r["formato_documento"],
            emisor=r["emisor"],
            contenido=r["contenido"]
        ))

def save_db():
    data = {}
    
    # Periodo
    data["periodo"] = {
        "nombre_periodo": periodo_actual.nombre_periodo,
        "fecha_inicio": periodo_actual.fecha_inicio,
        "fecha_final": periodo_actual.fecha_final,
        "estado_periodo": periodo_actual.estado_periodo
    }
    
    # Usuarios
    data["usuarios"] = {
        "coordinadores": [],
        "docentes": [],
        "estudiantes": []
    }
    
    for c in coordinadores.values():
        data["usuarios"]["coordinadores"].append({
            "cedula": c.cedula,
            "nombres": c.nombres,
            "apellidos": c.apellidos,
            "correo": c._correo,
            "contrasenia": getattr(c, "_Usuario__contrasenia", ""),
            "id_coordinador": c.id_coordinador,
            "fecha_asignacion_cargo": c.fecha_asignacion_cargo
        })
        
    for d in docentes.values():
        data["usuarios"]["docentes"].append({
            "cedula": d.cedula,
            "nombres": d.nombres,
            "apellidos": d.apellidos,
            "correo": d._correo,
            "contrasenia": getattr(d, "_Usuario__contrasenia", ""),
            "especialidad": d.especialidad
        })
        
    for e in estudiantes.values():
        data["usuarios"]["estudiantes"].append({
            "cedula": e.cedula,
            "nombres": e.nombres,
            "apellidos": e.apellidos,
            "correo": e._correo,
            "contrasenia": getattr(e, "_Usuario__contrasenia", ""),
            "id_estudiante": e._id_estudiante,
            "nombre_periodo": e.nombre_periodo,
            "tipo_matricula": e._tipo_matricula
        })
        
    # Materias
    data["materias"] = []
    for m in materias.values():
        data["materias"].append({
            "id_materia": m.id_materia,
            "nombre_materia": m.nombre_materia,
            "nota_minima": m.nota_minima,
            "asistencia_minima": m.asistencia_minima
        })
        
    # Secciones
    data["secciones"] = []
    for s in secciones.values():
        doc_emails = [d._correo for d in s.docentes]
        est_ids = [e._id_estudiante for e in s.estudiantes_inscritos]
        horarios_list = []
        for h in s.lista_horarios:
            horarios_list.append({
                "turno": h.turno,
                "hora_inicio": h.hora_inicio,
                "hora_fin": h.hora_fin,
                "modalidad": h._modalidad
            })
            
        av_dict = None
        if s.aula_virtual:
            av_dict = {
                "capacidad_maxima": s.aula_virtual.capacidad_maxima,
                "enlace_plataforma": s.aula_virtual._enlace_plataforma,
                "tipo_plataforma": s.aula_virtual._tipo_plataforma
            }
            
        data["secciones"].append({
            "id_seccion": s.id_seccion,
            "capacidad_estudiantil": s.capacidad_estudiantil,
            "materia_id": s.materia.id_materia if s.materia else "",
            "docentes_correos": doc_emails,
            "estudiantes_ids": est_ids,
            "horarios": horarios_list,
            "aula_virtual": av_dict
        })
        
    # Carreras
    data["carreras"] = [{
        "id_carrera": carrera_software.id_carrera,
        "nombre_carrera": carrera_software.nombre_carrera,
        "capacidad_estudiantil": carrera_software.capacidad_estudiantil
    }]
    
    # Notas
    data["notas"] = []
    for est in estudiantes.values():
        for n in est.historial.lista_nota_materia:
            data["notas"].append({
                "estudiante_id": est._id_estudiante,
                "materia_id": n.materia.id_materia,
                "parcial1": n.parcial1,
                "parcial2": n.parcial2,
                "asistencia": n.asistencia,
                "periodo_cerrado": getattr(n, "periodo_cerrado", False)
            })
            
    # Solicitudes de retiro
    data["solicitudes_retiro"] = []
    for sol in solicitudes_retiro:
        data["solicitudes_retiro"].append({
            "id": sol["id"],
            "estudiante_id": sol["estudiante_id"],
            "nombre": sol["nombre"],
            "correo": sol["correo"],
            "motivo": sol["motivo"],
            "fecha": sol["fecha"],
            "estado": sol["estado"]
        })
        
    # Reportes generados
    data["reportes_generados"] = []
    for rep in reportes_generados:
        data["reportes_generados"].append({
            "tipo_de_reporte": rep.tipo_de_reporte,
            "formato_documento": rep.formato_documento,
            "emisor": rep.emisor,
            "contenido": rep.contenido
        })
        
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Cargar base de datos al arrancar
load_db()

# =========================================================================
# HELPER FUNCTIONS
# =========================================================================
def obtener_usuario_por_correo(correo):
    # Buscar en Coordinadores
    user = coordinadores.get(correo)
    if user:
        return user, 'coordinador'
        
    # Buscar en Docentes
    user = docentes.get(correo)
    if user:
        return user, 'docente'
        
    # Buscar en Estudiantes
    user = estudiantes.get(correo)
    if user:
        return user, 'estudiante'
        
    return None, None

def verificar_contrasenia(usuario, contrasenia_ingresada):
    if not usuario:
        return False
    contrasenia_real = getattr(usuario, '_Usuario__contrasenia', None)
    return contrasenia_real == contrasenia_ingresada

# Nota: La propiedad 'esta_aprobado' se encuentra definida internamente en NotaMateria
# usando el patrón Observer y la verificación del estado del periodo. No se inyecta dinámicamente.


# =========================================================================
# RUTAS DE FLASK
# =========================================================================

@app.route('/')
def index():
    if 'usuario' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    correo = request.form.get('correo', '').strip()
    contrasenia = request.form.get('contrasenia', '').strip()

    usuario, rol = obtener_usuario_por_correo(correo)
    if usuario and verificar_contrasenia(usuario, contrasenia):
        session['usuario'] = correo
        session['rol'] = rol
        session['nombre'] = usuario.obtener_nombre_completo()
        
        if rol == 'estudiante':
            session['id'] = usuario._id_estudiante
        elif rol == 'coordinador':
            session['id'] = usuario.id_coordinador
        else:
            session['id'] = usuario.cedula
            
        return jsonify({"status": "success", "redirect": url_for('dashboard')})
    else:
        return jsonify({"status": "error", "message": "Credenciales inválidas. Por favor verifique el correo y la contraseña."})

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('index'))
    
    rol = session['rol']
    if rol == 'estudiante':
        return redirect(url_for('dashboard_estudiante'))
    elif rol == 'docente':
        return redirect(url_for('dashboard_docente'))
    elif rol == 'coordinador':
        return redirect(url_for('dashboard_coordinador'))
    return redirect(url_for('logout'))

# -------------------------------------------------------------------------
# RUTA ESTUDIANTE
# -------------------------------------------------------------------------
@app.route('/student')
def dashboard_estudiante():
    if 'usuario' not in session or session['rol'] != 'estudiante':
        return redirect(url_for('index'))
    
    est = estudiantes[session['usuario']]
    
    # Calificaciones
    notas_info = []
    for nota in est.historial.lista_nota_materia:
        estado_m = nota.esta_aprobado
        notas_info.append({
            "codigo": nota.materia.id_materia,
            "materia": nota.materia.nombre_materia,
            "parcial1": nota.parcial1,
            "parcial2": nota.parcial2,
            "nota_final": nota.nota_final,
            "asistencia": nota.asistencia,
            "estado": estado_m.value,
            "badge_class": "badge-success" if estado_m == EstadoDeAprobacionMateria.MATERIA_APROBADA else ("badge-danger" if estado_m == EstadoDeAprobacionMateria.MATERIA_REPROBADA else "badge-warning")
        })

    veredicto = est.esta_aprobado
    veredicto_badge = "badge-success" if veredicto == EstadoDeAprobacionNivelacion.APROBADO else ("badge-danger" if veredicto == EstadoDeAprobacionNivelacion.REPROBADO else "badge-warning")

    # Horarios
    horarios_info = []
    for sec in est.secciones_asociadas:
        for hor in sec.lista_horarios:
            resumen = hor.resumen_de_seccion(sec)
            horarios_info.append({
                "materia": sec.materia.nombre_materia,
                "seccion": sec.id_seccion,
                "turno": resumen["Turno de clase"],
                "inicio": resumen["Inicializacion"],
                "fin": resumen["Terminacion"],
                "modalidad": resumen["Modalidad"],
                "docente": resumen["Docente"]
            })

    mis_reportes = [r for r in reportes_generados if r.emisor == est.obtener_nombre_completo()]

    return render_template(
        'dashboard_estudiante.html',
        estudiante=est,
        notas=notas_info,
        promedio=est.historial.promedio_general,
        veredicto=veredicto.value,
        veredicto_badge=veredicto_badge,
        horarios=horarios_info,
        reportes=mis_reportes,
        periodo=periodo_actual.nombre_periodo,
        estado_periodo=periodo_actual.estado_periodo
    )

@app.route('/student/request_certificate', methods=['POST'])
def student_request_certificate():
    if 'usuario' not in session or session['rol'] != 'estudiante':
        return jsonify({"status": "error", "message": "No autorizado"})
    
    est = estudiantes[session['usuario']]
    formato = request.form.get('formato', 'PDF')
    
    reporte = est.solicitar_certificado(formato_documento=formato)
    reportes_generados.append(reporte)
    
    save_db() # Guardar base de datos
    return jsonify({
        "status": "success", 
        "message": "Certificado solicitado con éxito", 
        "report_content": reporte.imprimir_reporte()
    })

@app.route('/student/request_withdrawal', methods=['POST'])
def student_request_withdrawal():
    if 'usuario' not in session or session['rol'] != 'estudiante':
        return jsonify({"status": "error", "message": "No autorizado"})
    
    est = estudiantes[session['usuario']]
    motivo = request.form.get('motivo', '').strip()
    formato = request.form.get('formato', 'Consola')
    
    if not motivo:
        return jsonify({"status": "error", "message": "Debe especificar un motivo para el retiro."})
    
    reporte = est.solicitar_retiro(motivo=motivo, formato_documento=formato)
    
    solicitudes_retiro.append({
        "id": len(solicitudes_retiro) + 1,
        "estudiante_id": est._id_estudiante,
        "nombre": est.obtener_nombre_completo(),
        "correo": est._correo,
        "motivo": motivo,
        "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
        "estado": "Pendiente",
        "reporte": reporte
    })
    
    save_db() # Guardar base de datos
    return jsonify({"status": "success", "message": "Solicitud de retiro enviada correctamente al Coordinador."})


# -------------------------------------------------------------------------
# RUTA DOCENTE
# -------------------------------------------------------------------------
@app.route('/teacher')
def dashboard_docente():
    if 'usuario' not in session or session['rol'] != 'docente':
        return redirect(url_for('index'))
    
    doc = docentes[session['usuario']]
    
    secciones_info = []
    for sec in doc.secciones:
        alumnos_sec = []
        for al in sec.estudiantes_inscritos:
            nota_obj = next((n for n in al.historial.lista_nota_materia if n.materia.id_materia == sec.materia.id_materia), None)
            
            alumnos_sec.append({
                "cedula": al.cedula,
                "nombre": al.obtener_nombre_completo(),
                "id_estudiante": al._id_estudiante,
                "parcial1": nota_obj.parcial1 if nota_obj else 0.0,
                "parcial2": nota_obj.parcial2 if nota_obj else 0.0,
                "asistencia": nota_obj.asistencia if nota_obj else 0,
                "nota_final": nota_obj.nota_final if nota_obj else 0.0,
                "estado_aprobacion": (nota_obj.esta_aprobado.value if nota_obj else "Sin Nota")
            })
            
        secciones_info.append({
            "id_seccion": sec.id_seccion,
            "materia": sec.materia.nombre_materia,
            "capacidad": sec.capacidad_estudiantil,
            "cupos_libres": sec.verificar_cupos_disponibles(),
            "inscritos_count": len(sec.estudiantes_inscritos),
            "estudiantes": alumnos_sec
        })

    mis_reportes = [r for r in reportes_generados if r.emisor == doc.obtener_nombre_completo()]
    
    # Calcular promedio
    todas_notas = []
    for sec in doc.secciones:
        for al in sec.estudiantes_inscritos:
            nota_obj = next((n for n in al.historial.lista_nota_materia if n.materia.id_materia == sec.materia.id_materia), None)
            if nota_obj:
                todas_notas.append(nota_obj.nota_final)
    promedio_doc = sum(todas_notas) / len(todas_notas) if todas_notas else 0.0

    return render_template(
        'dashboard_docente.html',
        docente=doc,
        secciones=secciones_info,
        promedio_rendimiento=promedio_doc,
        reportes=mis_reportes,
        estado_periodo=periodo_actual.estado_periodo
    )

@app.route('/teacher/student_info/<student_id>')
def teacher_student_info(student_id):
    if 'usuario' not in session or session['rol'] != 'docente':
        return jsonify({"status": "error", "message": "No autorizado"}), 403
        
    est = next((e for e in estudiantes.values() if e._id_estudiante == student_id), None)
    if not est:
        return jsonify({"status": "error", "message": "Estudiante no encontrado"}), 404
        
    notas_info = []
    for nota in est.historial.lista_nota_materia:
        notas_info.append({
            "materia": nota.materia.nombre_materia,
            "parcial1": nota.parcial1,
            "parcial2": nota.parcial2,
            "asistencia": nota.asistencia,
            "nota_final": nota.nota_final,
            "estado": nota.esta_aprobado.value
        })
        
    est_data = {
        "id_estudiante": est._id_estudiante,
        "nombres": est.nombres,
        "apellidos": est.apellidos,
        "correo": est._correo,
        "cedula": est.cedula,
        "nombre_periodo": est.nombre_periodo,
        "tipo_matricula": est._tipo_matricula,
        "notas": notas_info,
        "promedio": est.historial.promedio_general
    }
    
    return jsonify({"status": "success", "data": est_data})

@app.route('/teacher/save_grades', methods=['POST'])
def teacher_save_grades():
    if 'usuario' not in session or session['rol'] != 'docente':
        return jsonify({"status": "error", "message": "No autorizado"})
    
    if periodo_actual.estado_periodo == "Finalizado":
        return jsonify({"status": "error", "message": "No se pueden modificar calificaciones. El período académico ya está cerrado."})
        
    estudiante_id = request.form.get('estudiante_id')
    seccion_id = request.form.get('seccion_id')
    
    try:
        parcial1 = float(request.form.get('parcial1', 0.0))
        parcial2 = float(request.form.get('parcial2', 0.0))
        asistencia = int(request.form.get('asistencia', 0))
    except ValueError:
        return jsonify({"status": "error", "message": "Valores de calificaciones o asistencia inválidos."})

    est = next((e for e in estudiantes.values() if e._id_estudiante == estudiante_id), None)
    sec = secciones.get(seccion_id)

    if not est or not sec:
        return jsonify({"status": "error", "message": "Estudiante o Sección no encontrados."})

    nota_obj = next((n for n in est.historial.lista_nota_materia if n.materia.id_materia == sec.materia.id_materia), None)
    if nota_obj:
        nota_obj.parcial1 = parcial1
        nota_obj.parcial2 = parcial2
        nota_obj.asistencia = asistencia
    else:
        est.historial.crear_nota_materia(
            materia=sec.materia,
            periodo=periodo_actual,
            parcial1=parcial1,
            parcial2=parcial2,
            asistencia=asistencia
        )

    save_db() # Guardar base de datos
    return jsonify({"status": "success", "message": f"Notas de {est.obtener_nombre_completo()} guardadas con éxito."})

@app.route('/teacher/generate_report', methods=['POST'])
def teacher_generate_report():
    if 'usuario' not in session or session['rol'] != 'docente':
        return jsonify({"status": "error", "message": "No autorizado"})
    
    doc = docentes[session['usuario']]
    tipo = request.form.get('tipo_reporte', 'Reporte de Notas')
    formato = request.form.get('formato', 'PDF')
    contenido = request.form.get('contenido', '').strip()
    
    if not contenido:
        return jsonify({"status": "error", "message": "El contenido del reporte no puede estar vacío."})
        
    reporte = doc.realizaReporte(tipo_de_reporte=tipo, formato_documento=formato, contenido=contenido)
    reportes_generados.append(reporte)
    
    save_db() # Guardar base de datos
    return jsonify({
        "status": "success",
        "message": "Reporte docente generado con éxito.",
        "report_content": reporte.imprimir_reporte()
    })


# -------------------------------------------------------------------------
# RUTA COORDINADOR
# -------------------------------------------------------------------------
@app.route('/coordinator')
def dashboard_coordinador():
    if 'usuario' not in session or session['rol'] != 'coordinador':
        return redirect(url_for('index'))
    
    coord = coordinadores[session['usuario']]
    
    # Secciones
    secciones_info = []
    for sec in secciones.values():
        docentes_nombres = ", ".join(d.obtener_nombre_completo() for d in sec.docentes) if sec.docentes else "Sin Docente"
        secciones_info.append({
            "id_seccion": sec.id_seccion,
            "materia": sec.materia.nombre_materia,
            "capacidad": sec.capacidad_estudiantil,
            "inscritos": len(sec.estudiantes_inscritos),
            "docente": docentes_nombres,
            "aula": sec.aula_virtual._enlace_plataforma if sec.aula_virtual else "No asignada",
            "disponibilidad": "Disponible" if sec.disponibilidad else "Lleno"
        })

    docentes_lista = [{"correo": d._correo, "nombre": d.obtener_nombre_completo()} for d in docentes.values()]
    materias_lista = [{"id": m.id_materia, "nombre": m.nombre_materia} for m in materias.values()]

    # Estadísticas
    total_estudiantes = len(estudiantes)
    total_aprobados = sum(1 for e in estudiantes.values() if e.esta_aprobado == EstadoDeAprobacionNivelacion.APROBADO)
    total_reprobados = sum(1 for e in estudiantes.values() if e.esta_aprobado == EstadoDeAprobacionNivelacion.REPROBADO)
    total_pendientes = sum(1 for e in estudiantes.values() if e.esta_aprobado == EstadoDeAprobacionNivelacion.PENDIENTE)

    return render_template(
        'dashboard_coordinador.html',
        coordinador=coord,
        periodo=periodo_actual,
        secciones=secciones_info,
        docentes=docentes_lista,
        materias=materias_lista,
        solicitudes=solicitudes_retiro,
        stats={
            "total": total_estudiantes,
            "aprobados": total_aprobados,
            "reprobados": total_reprobados,
            "pendientes": total_pendientes
        }
    )

@app.route('/coordinator/toggle_period', methods=['POST'])
def coordinator_toggle_period():
    if 'usuario' not in session or session['rol'] != 'coordinador':
        return jsonify({"status": "error", "message": "No autorizado"})
    
    accion = request.form.get('accion')
    coord = coordinadores[session['usuario']]

    if accion == "iniciar":
        coord.abrir_periodo_matricula(periodo_actual)
        msg = "El periodo académico ha sido INICIADO. Los estudiantes pueden inscribirse y los docentes colocar notas."
    elif accion == "finalizar":
        coord.cerrar_periodo_matricula(periodo_actual)
        for est in estudiantes.values():
            for nota in est.historial.lista_nota_materia:
                nota.periodo_cerrado = True
            est.historial.actualizar()
        msg = "El periodo académico ha sido FINALIZADO. Se han consolidado todas las notas finales y actas."
    else:
        return jsonify({"status": "error", "message": "Acción no válida"})

    save_db() # Guardar base de datos
    return jsonify({
        "status": "success", 
        "message": msg, 
        "estado_actual": periodo_actual.estado_periodo
    })

@app.route('/coordinator/approve_withdrawal', methods=['POST'])
def coordinator_approve_withdrawal():
    if 'usuario' not in session or session['rol'] != 'coordinador':
        return jsonify({"status": "error", "message": "No autorizado"})
        
    solicitud_id = int(request.form.get('solicitud_id', 0))
    accion = request.form.get('accion', '')
    
    sol = next((s for s in solicitudes_retiro if s['id'] == solicitud_id), None)
    if not sol:
        return jsonify({"status": "error", "message": "Solicitud no encontrada."})

    est = estudiantes.get(sol['correo'])
    
    if accion == 'aprobar':
        sol['estado'] = 'Aprobado'
        if est:
            for sec in list(est.secciones_asociadas):
                sec.liberar_cupo(est)
                est.secciones_asociadas.remove(sec)
        msg = f"Retiro aprobado. {sol['nombre']} ha sido desvinculado de todas las asignaturas."
    else:
        sol['estado'] = 'Rechazado'
        msg = f"Solicitud de retiro para {sol['nombre']} rechazada."

    save_db() # Guardar base de datos
    return jsonify({"status": "success", "message": msg})

@app.route('/coordinator/create_section', methods=['POST'])
def coordinator_create_section():
    if 'usuario' not in session or session['rol'] != 'coordinador':
        return jsonify({"status": "error", "message": "No autorizado"})
    
    id_seccion = request.form.get('id_seccion', '').strip().upper()
    capacidad = request.form.get('capacidad')
    materia_id = request.form.get('materia_id')
    
    if not id_seccion or not capacidad or not materia_id:
        return jsonify({"status": "error", "message": "Todos los campos son obligatorios para crear la sección."})
        
    try:
        capacidad = int(capacidad)
    except ValueError:
        return jsonify({"status": "error", "message": "La capacidad debe ser un número entero."})

    if id_seccion in secciones:
        return jsonify({"status": "error", "message": f"Ya existe una sección con el código {id_seccion}."})

    materia_obj = materias.get(materia_id)
    if not materia_obj:
        return jsonify({"status": "error", "message": "Materia no encontrada."})

    coord = coordinadores[session['usuario']]

    try:
        nueva_sec = (SeccionBuilder()
                    .con_id_seccion(id_seccion)
                    .con_capacidad_estudiantil(capacidad)
                    .con_materia(materia_obj)
                    .con_coordinador(coord)
                    .build())
        
        nueva_sec.agregar_horario(Horario("Matutino", "07:00", "09:00", "Presencial"))
        secciones[id_seccion] = nueva_sec
        
        save_db() # Guardar base de datos
        return jsonify({"status": "success", "message": f"Sección {id_seccion} creada exitosamente para {materia_obj.nombre_materia}."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error al crear sección con Builder: {e}"})

@app.route('/coordinator/assign_teacher', methods=['POST'])
def coordinator_assign_teacher():
    if 'usuario' not in session or session['rol'] != 'coordinador':
        return jsonify({"status": "error", "message": "No autorizado"})
        
    seccion_id = request.form.get('seccion_id')
    docente_correo = request.form.get('docente_correo')
    
    sec = secciones.get(seccion_id)
    doc = docentes.get(docente_correo)
    
    if not sec or not doc:
        return jsonify({"status": "error", "message": "Sección o Docente no encontrados."})
        
    sec.asignar_docente(doc)
    
    save_db() # Guardar base de datos
    return jsonify({"status": "success", "message": f"Docente {doc.obtener_nombre_completo()} asignado con éxito a la sección {sec.id_seccion}."})

@app.route('/coordinator/generate_career_report', methods=['POST'])
def coordinator_generate_career_report():
    if 'usuario' not in session or session['rol'] != 'coordinador':
        return jsonify({"status": "error", "message": "No autorizado"})
        
    formato = request.form.get('formato', 'PDF')
    
    carrera_software.estudiantes_inscritos = len(estudiantes)
    reporte = carrera_software.mostrar_datos_carrera(formato_documento=formato)
    reportes_generados.append(reporte)
    
    save_db() # Guardar base de datos
    return jsonify({
        "status": "success",
        "message": "Reporte de carrera generado con éxito.",
        "report_content": reporte.imprimir_reporte()
    })

# =========================================================================
# LANZADOR DE LA APLICACIÓN
# =========================================================================

if __name__ == '__main__':
    port = 5000
    
    flask_thread = threading.Thread(
        target=lambda: app.run(host='127.0.0.1', port=port, debug=False, use_reloader=False),
        daemon=True
    )
    flask_thread.start()
    
    print("--------------------------------------------------")
    print(f" Servidor local activo en: http://127.0.0.1:{port}")
    print(" Intentando iniciar ventana WebView nativa...")
    print("--------------------------------------------------")
    
    time.sleep(1.2)
    
    try:
        import webview
        webview.create_window(
            title='Sistema de Gestión de Nivelación - ULEAM', 
            url=f'http://127.0.0.1:{port}', 
            width=1200, 
            height=820,
            resizable=True,
            min_size=(1000, 600)
        )
        webview.start()
    except Exception as e:
        print(f"\n[AVISO] No se pudo lanzar pywebview automáticamente ({e}).")
        print("Abriendo en el navegador predeterminado...")
        webbrowser.open(f'http://127.0.0.1:{port}')
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nServidor detenido por el usuario.")
