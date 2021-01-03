class Sistema:
    def __init__(self):
        self.activo = True

    def show_menu(self):
        #Print para mostrar menu
        print("Menú\n   1) - Agrear Alumno\n   2) - Agregar Curso\n   3) - Agregar notas a alumno\n   4) - Agregar docente\n   5) - Mostrar promedios\n   6) - Exportar datos\n   7) - Salir\n")

        #Se pregunta por el numero
        while True:
            opcion = input('Ingresa el N° : ')
            if opcion.isnumeric() and opcion in ['1','2','3','4','5','6','7']:
                break
            else:
                print('Opcion no valida.')

        return int(opcion)


class Alumnos:
    def __init__(self):
        self.alumnos = [['1','Raul Sanchez (valor por defecto)',21,'45215125']]

    def agregar_alumno(self, nombre, edad, dni):
        alumno = [str(len(self.alumnos)+1),nombre ,edad ,dni]
        self.alumnos.append(alumno)
        print('Alumno '+nombre+' fue agregado, hay '+str(len(self.alumnos))+' en total.')

    def exportar_alumnos(self):
        texto = []
        for alumno in self.alumnos:
            texto.append('N°: '+str(alumno[0])+', Alumno: '+alumno[1]+', Edad: '+str(alumno[2])+', DNI: '+alumno[3]+'\n')

        file = open('alumnos.txt','w')
        for linea in texto:
            file.write(linea)
        file.close()
        print('Archivo "alumnos.txt" creado exitosamente.')


class Cursos:
    def __init__(self):
        self.cursos = [['1','Geometria (valor por defecto)']]

    def agregar_curso(self,nombre):
        curso = [str(len(self.cursos)+1),nombre]
        self.cursos.append(curso)
        print('Curso "'+curso[1]+'" fue agregado.')

    def exportar_cursos(self):
        texto = []
        for curso in self.cursos:
            texto.append('N°: '+str(curso[0])+', Nombre: '+curso[1]+'\n')

        file = open('cursos.txt','w')
        for linea in texto:
            file.write(linea)
        file.close()
        print('Archivo "cursos.txt" creado exitosamente.')

class Docentes:
    def __init__(self):
        self.docentes = [['1','Juan Perez (valor por defecto)',29,'458204330']]

    def agregar_docente(self,nombre,edad,dni):
        docente = [str(len(self.docentes) + 1),nombre,edad,dni]
        self.docentes.append(docente)
        print('Docente '+docente[1]+' fue agregado.')

    def exportar_docentes(self):
        texto = []
        for docente in self.docentes:
            texto.append('N°: '+str(docente[0])+', Docente: '+docente[1]+', Edad: '+str(docente[2])+', DNI: '+docente[3]+'\n')

        file = open('docentes.txt','w')
        for linea in texto:
            file.write(linea)
        file.close()
        print('Archivo "docentes.txt" creado exitosamente.')

class Notas:
    def __init__(self):
        self.notas = [[1, '1', '1', [10, 20], 20, 10, 15.0]]

    def agregar_nota(self, n_alumno, n_curso, valor_nota):
        existe = False
        print(f'Agregando nota con valores n_alumno:{n_alumno}, n_curso: {n_curso} y nota:{valor_nota}')

        for nota in self.notas:
            if nota[1] == n_alumno and nota[2] == n_curso:
                print('Alumno existente en curso dado, modificando...')
                if len(nota[3]) >= 4:
                    print('Alumno seleccionado ya tiene sus 4 notas.')
                    break

                notas_alumno = nota[3]+[valor_nota]
                nota_maxima = max(notas_alumno)
                nota_minima = min(notas_alumno)
                promedio = sum(notas_alumno)/len(notas_alumno)
                nota = [nota[0],n_alumno,n_curso,notas_alumno,nota_maxima,nota_minima,promedio]
                existe = True

        if not existe:
            print('Alumno no existente en curso dado, agregando...')
            notas_alumno = [valor_nota]
            nota_maxima = max(notas_alumno)
            nota_minima = min(notas_alumno)
            promedio = sum(notas_alumno)/len(notas_alumno)
            nota = [len(self.notas)+1, n_alumno, n_curso, notas_alumno, nota_maxima, nota_minima, promedio]
        self.notas.append(nota)

    def promedios(self,alumnos):
        print('Mostrando promedios: ')
        for alumno in alumnos:
            n_alumno = alumno[0]
            nombre = alumno[1]
            for nota in self.notas:
                if nota[1] == n_alumno:
                    print('  Curso: '+nota[2]+' Alumno: '+nombre+' Promedio: '+str(nota[-1]))

    def exportar_notas(self):
        texto = []
        for nota in self.notas:
            lista_notas = []
            for n in nota[3]:
                lista_notas.append(str(n))
            texto.append('N°: '+str(nota[0])+', Alumno: '+nota[1]+', Curso: '+nota[2]+', notas: ['+','.join(lista_notas)+'], nota máxima: '+str(nota[4])+', nota minima: '+str(nota[5])+', promedio: '+str(nota[5])+'\n')

        file = open('notas.txt','w')
        for linea in texto:
            file.write(linea)
        file.close()
        print('Archivo "notas.txt" creado exitosamente.')
