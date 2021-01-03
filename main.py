from objetos import *

sistema = Sistema()
alumnos_object = Alumnos()
cursos_object = Cursos()
docentes = Docentes()
notas = Notas()

while sistema.activo:
    opcion = sistema.show_menu()

    if opcion == 1:

        print('Agregando alumno: ')
        #Agregando un nuevo alumno
        while True:
            nombre_alumno = input('   Nombre alumno: ')
            edad_alumno = input('   Edad del alumno: ')
            dni_alumno = input('   DNI del alumno: ')

            if edad_alumno.isnumeric():
                break
            else:
                print('Edad no numerica.')

        alumnos_object.agregar_alumno(nombre_alumno, edad_alumno, dni_alumno)

    elif opcion == 2:
        print('Agregando curso: ')

        nombre_curso = input('   Nombre curso: ')

        cursos_object.agregar_curso(nombre_curso)

    elif opcion == 3:
        #eligiendo un alumno:
        print('Agregando nota a alumno: ')
        print('   Eliga a que alumno agregar una nota: ')

        for alumno in alumnos_object.alumnos:
            print('   '+alumno[0]+') - '+alumno[1])

        while True:
            n_alumno = input('   Numero Alumno: ')

            if n_alumno.isnumeric() == False:
                print('    La opcion debe ser un numero.')

            elif int(n_alumno) < 1 or int(n_alumno) > len(alumnos_object.alumnos):
                print('    El numero debe estar en la lista mostrada.',n_alumno)
            else:
                break

        alumno = alumnos_object.alumnos[int(n_alumno) - 1]

        print('   Elija un curso: ')

        for curso in cursos_object.cursos:
            print('    '+curso[0]+') - '+curso[1])

        while True:
            n_curso = input('   Numero Curso: ')

            if n_curso.isnumeric() == False:
                print('    La opcion debe ser un numero.')

            elif int(n_curso) < 1 or int(n_curso) > len(cursos_object.cursos):
                print('    El numero debe estar en la lista mostrada.',n_curso)

            else:
                break

        curso = cursos_object.cursos[int(n_curso) - 1]

        while True:
            nota = input('   Nota a agregar: ')
            if nota.isnumeric():
                nota = int(nota)
                if nota >= 0 and nota <= 20:
                    break
                else:
                    print('Nota fuera de rango [0, 20]')
            else:
                print('Nota no es numerica.')

        notas.agregar_nota(alumno[0],curso[0],nota)

    elif opcion == 4:
        print('Agregando docente: ')

        nombre_docente = input('   Nombre docente: ')
        while True:
            edad_docente = input('   Edad del docente: ')
            if edad_docente.isnumeric():
                break
            else:
                print('    Edad no numerica')
        dni_docente = input('   DNI del docente: ')

        docentes.agregar_docente(nombre_docente,edad_docente,dni_docente)

    elif opcion == 5:
        notas.promedios(alumnos_object.alumnos)

    elif opcion == 6:
        notas.exportar_notas()
        alumnos_object.exportar_alumnos()
        cursos_object.exportar_cursos()
        docentes.exportar_docentes()

    elif opcion == 7:
        sistema.activo = False
