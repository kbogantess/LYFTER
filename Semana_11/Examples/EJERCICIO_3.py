############################################################################ INICIO PROGRAMA


import csv
import os


class Student:
    
    def __init__(self, name, section, spanish_note, english_note, social_studies, science_note):
        
        self.name = name
        self.section = section
        self.spanish_note = spanish_note
        self.english_note = english_note
        self.social_studies = social_studies
        self.science_note = science_note

    def average(self):
        return (self.spanish_note + self.english_note + self.social_studies + self.science_note) / 4


############################################################################ INICIO VARIABLES PRINCIPALES


while True:
    try:
        n = int(input("Digite la cantidad de estudiantes que desea ingresar: "))
        break
    except ValueError as ex:
        print(f"ingrese un valor entero... {ex}")

students_list = []


############################################################################ INICIO MENU:



while True:

    try:
        menu = int(input("""

    Digite una opción del menú:

    (1) --->  Ingresar información de n cantidad de estudiantes, uno por uno
    (2) --->  Ver la información de todos los estudiantes ingresados                    
    (3) --->  Ver el top 3 de los estudiantes con la mejor nota promedio
    (4) --->  Ver la nota promedio entre las notas de todos los estudiantes
    (5) --->  Exportar datos actuales a un CSV
    (6) --->  Importar los datos de un archivo CSV previamente exportado
    (7) --->  Salir

"""))

    except ValueError as ex:
        print(f"ingresó un valor incorrecto, intente nuevamente...{ex} ")
        continue


############################################################################ CIERRE MENU
############################################################################ INICIO PRIMER OPCIÓN



    if menu == 1:
        for i in range(n):  

            name =     input("Digite el nombre: ")
            section =  input("Digite la sección del estudiante: ")

            while True:
                try:
                    spanish_grade = float(input("Digite la nota de español: "))
                    break
                except ValueError as ex:
                    print(f"Los valores deben ser números, intente de nuevo...{ex}")

            while True:
                try:       
                    english_grade = float(input("Digite la nota de inglés: "))
                    break
                except ValueError as ex:
                    print(f"Los valores deben ser números, intente de nuevo...{ex}")

            while True:
                try:       
                    social_studies_grade = float(input("Digite la nota de estudios sociales: "))
                    break
                except ValueError as ex:
                    print(f"Los valores deben ser números, intente de nuevo...{ex}")

            while True:
                try:       
                    science_grade = float(input("Digite la nota de ciencias: "))
                    break
                except ValueError as ex:
                    print(f"Los valores deben ser números, intente de nuevo...{ex}")

            student = Student(name, section, spanish_grade, english_grade, social_studies_grade, science_grade)
            students_list.append(student)  



############################################################################ FINALIZA PRIMER OPCIÓN
############################################################################ INICIA SEGUNDA OPCIÓN



    elif menu == 2:

        if not students_list:
            print("Debe registrar a los estudiantes primero ")

        else:
            for student in students_list:
                print(
                    f"Nombre: {student.name}, Sección: {student.section}, "
                    f"Español: {student.spanish_note}, Inglés: {student.english_note}, "
                    f"Estudios Sociales: {student.social_studies}, Ciencias: {student.science_note}"
                )



############################################################################ FINALIZA SEGUNDA OPCIÓN
############################################################################ INICIA TERCER OPCIÓN



    elif menu == 3:
        print("TOP 3 de estudiantes con las mejores notas promedio: ")

        students_sorted = sorted(students_list, key=lambda s: s.average(), reverse=True)

        for student in students_sorted[:3]:
            print(f"Nombre: {student.name}, Promedio: {student.average()}")



############################################################################ FINALIZA TERCER OPCIÓN
############################################################################ INICIA CUARTA OPCIÓN



    elif menu == 4:
        print("Nota promedio entre las notas promedio: ")

        if not students_list:
            print("Debe registrar a los estudiantes primero ")

        else:
            overall_average = sum(student.average() for student in students_list) / len(students_list)
            print(f"El promedio general de todos los estudiantes es: {overall_average}")



############################################################################ FINALIZA CUARTA OPCIÓN
############################################################################ INICIA QUINTA OPCIÓN



    elif menu == 5:
        if not students_list:
            print("Debe registrar a los estudiantes primero ")
        else:
            filename = "students.csv"
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Section", "Spanish", "English", "Social Studies", "Science"])
                for student in students_list:
                    writer.writerow([student.name, student.section, student.spanish_note, student.english_note,
                                    student.social_studies, student.science_note])
            print(f"Datos exportados exitosamente a {filename}")



############################################################################ FINALIZA QUINTA OPCIÓN
############################################################################ INICIA SEXTA OPCIÓN



    elif menu == 6:
        filename = "students.csv"
        if not os.path.exists(filename): 
            print("El archivo CSV con los datos no existe, exporte los datos primero ")
        else:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                students_list = [
                    Student(row["Name"], row["Section"], float(row["Spanish"]), float(row["English"]),
                            float(row["Social Studies"]), float(row["Science"]))
                    for row in reader
                ]
            print("Datos importados exitosamente del archivo CSV.")    



############################################################################ FINALIZA SEXTA OPCIÓN
############################################################################ INICIA SÉTIMA OPCIÓN



    elif menu == 7:
        print("Finalizó el programa")
        break

    else:
        print("Opción no válida")



############################################################################ FINALIZA SÉTIMA OPCIÓN

############################################################################ FIN PROGRAMA
