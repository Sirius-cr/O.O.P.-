import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.academico.Clase_AulaVirtual import AulaVirtual
from models.academico.Clase_Horario import Horario
from models.academico.Clase_MallaCurricular import MallaCurricular
from models.academico.Clase_Materia import Materia
from models.academico.Clase_Periodo import Periodo
from models.academico.Clase_Seccion import Seccion
from models.academico.Clase_ofertaAcadémica import OfertaAcademica


def menu():
    print("\n===== SISTEMA ACADÉMICO =====")
    print("1. Crear Aula Virtual")
    print("2. Crear Materia")
    print("3. Crear Malla Curricular")
    print("4. Crear Periodo")
    print("5. Crear Oferta Académica")
    print("6. Crear Sección")
    print("7. Crear Horario")
    print("8. Ver estructura")
    print("9. Salir")

def ver_estructura_sistema(periodo=None, malla=None, materia=None, seccion=None, aula=None):
    print("\n========== ESTRUCTURA DEL SISTEMA ACADÉMICO ==========\n")

    # =========================
    # PERIODO
    # =========================
    if periodo:
        print(f"PERIODO: {periodo.nombre_periodo}")
        print(f"   Estado: {periodo.estado_periodo}")
        print(f"   Fechas: {periodo.fecha_inicio} → {periodo.fecha_final}")

        print("   Ofertas académicas:")
        if periodo.ofertas_academicas:
            for i, oferta in enumerate(periodo.ofertas_academicas, 1):
                print(f"      {i}. Cupos: {oferta.cupos_disponibles}")
        else:
            print("      (Sin ofertas)")

    # =========================
    # MALLA
    # =========================
    if malla:
        print(f"\nMALLA: {malla.codigo_malla}")
        print(f"   Área: {malla.area_conocimiento}")

        print("   Materias:")
        if malla.lista_materias:
            for i, mat in enumerate(malla.lista_materias, 1):
                print(f"      {i}. {mat.nombre_materia}")
        else:
            print("      (Sin materias)")

    # =========================
    # MATERIA
    # =========================
    if materia:
        print(f"\nMATERIA: {materia.nombre_materia}")
        print(f"   ID: {materia.id_materia}")

        print("   Secciones:")
        if materia.secciones:
            for i, sec in enumerate(materia.secciones, 1):
                print(f"      {i}. Sección {sec.id_seccion} - Estudiantes: {len(sec.estudiantes_inscritos)}")
        else:
            print("      (Sin secciones)")

    # =========================
    # SECCION
    # =========================
    if seccion:
        print(f"\nSECCIÓN: {seccion.id_seccion}")
        print(f"   Capacidad: {seccion.capacidad_estudiantil}")
        print(f"   Estudiantes inscritos: {len(seccion.estudiantes_inscritos)}")
        print(f"   Docentes asignados: {len(seccion.docentes)}")

        print("   Horarios:")
        if seccion.lista_horarios:
            for i, h in enumerate(seccion.lista_horarios, 1):
                print(f"      {i}. {h.turno} ({h.hora_inicio}-{h.hora_fin})")
        else:
            print("      (Sin horarios)")

        print("   Entorno:")
        if seccion.entorno_asignado:
            print("      Asignado")
        else:
            print("      Sin entorno")

    # =========================
    # AULA VIRTUAL
    # =========================
    if aula:
        print(f"\nAULA VIRTUAL:")
        print(f"   Capacidad: {aula.capacidad_maxima}")
        print(f"   Tipo: {aula._tipo_plataforma}")
        print(f"   Acceso: {aula.obtener_acceso()}")

    print("\n======================================================\n")

def main():

    aula = None
    materia = None
    malla = None
    periodo = None
    oferta = None
    seccion = None
    horario = None

    while True:
        menu()
        op = input("Seleccione una opción: ")

        match op:

            # =========================
            # AULA VIRTUAL
            # =========================
            case "1":
                cap = int(input("Capacidad máxima: "))
                link = input("Enlace plataforma: ")
                tipo = input("Tipo plataforma: ")

                aula = AulaVirtual(cap, link, tipo)
                print("Aula creada. Acceso:", aula.obtener_acceso())

            # =========================
            # MATERIA
            # =========================
            case "2":
                idm = int(input("ID materia: "))
                nombre = input("Nombre materia: ")

                materia = Materia(idm, nombre)
                print(" Materia creada")

            # =========================
            # MALLA CURRICULAR
            # =========================
            case "3":
                cod = input("Código malla: ")
                area = input("Área conocimiento: ")

                malla = MallaCurricular(cod, area)
                print(" Malla creada")

                if materia:
                    malla.agregar_materias(materia)
                    print(" Materia agregada a la malla")

            # =========================
            # PERIODO
            # =========================
            case "4":
                nombre = input("Nombre periodo: ")
                ini = input("Fecha inicio: ")
                fin = input("Fecha fin: ")

                periodo = Periodo(nombre, ini, fin)
                print("Periodo creado")

                while True:
                    sub = input("Iniciar (i), Finalizar (f), Salir (s): ")

                    match sub:
                        case "i":
                            periodo.iniciar_periodo()
                        case "f":
                            periodo.finalizar_periodo()
                        case "s":
                            break
                        case _:
                            print("Opción inválida")

            # =========================
            # OFERTA ACADEMICA
            # =========================
            case "5":
                if periodo and malla:
                    cupos = int(input("Cupos disponibles: "))
                    oferta = OfertaAcademica(periodo, malla, cupos)
                    print("Oferta creada")
                else:
                    print(" Debes crear Periodo y Malla primero")

            # =========================
            # SECCION
            # =========================
            case "6":
                if materia:
                    id_sec = int(input("ID sección: "))
                    cap = int(input("Capacidad: "))

                    seccion = materia.crear_seccion(id_sec, cap)
                    print("Sección creada")

                    while True:
                        sub = input("Agregar estudiante (a), Ver cupos (v), Salir (s): ")

                        match sub:
                            case "a":
                                est = input("Nombre estudiante: ")
                                print(seccion.actualizar_estudiantes_inscritos(est))

                            case "v":
                                print("Cupos disponibles:", seccion.verificar_cupos_disponibles())

                            case "s":
                                break

                            case _:
                                print("Opción inválida")
                else:
                    print("Debes crear una materia primero")

            # =========================
            # HORARIO
            # =========================
            case "7":
                turno = input("Turno: ")
                ini = input("Hora inicio: ")
                fin = input("Hora fin: ")
                modal = input("Modalidad: ")

                horario = Horario(turno, ini, fin, modal)
                print("Horario creado")

                if seccion:
                    print(horario.resumen_de_seccion(seccion))
            case "8":
                ver_estructura_sistema(periodo, malla, materia, seccion, aula)
            case "9":
                print("Saliendo del sistema...")
                break

            case _:
                print("Opción inválida")


if __name__ == "__main__":
    main()