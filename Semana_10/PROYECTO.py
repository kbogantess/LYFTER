############################################################################ INICIO PROGRAMA



import csv
import os



while True:
    try:
        n = int(input("Digite la cantidad de estudiantes que desea ingresar: "))
    except ValueError as ex:
        print(f"ingrese un valor entero... {ex}")
    break

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

            student_info = {  
                "name": name,
                "section": section,
                "spanish_note": spanish_grade,
                "english_note": english_grade,
                "social_studies": social_studies_grade,
                "science_note": science_grade,
            }

            students_list.append(student_info)  



############################################################################ FINALIZA PRIMER OPCIÓN
############################################################################ INICIA SEGUNDA OPCIÓN



    elif menu == 2:

        if not students_list:
            print("Debe registrar a los estudiantes primero ")

        else:
            for i in students_list:
                
                print(
                    f"Nombre: {i['name']}, Sección: {i['section']}, "
                    f"Español: {i['spanish_note']}, Inglés: {i['english_note']}, "
                    f"Estudios Sociales: {i['social_studies']}, Ciencias: {i['science_note']}"
                    )



############################################################################ FINALIZA SEGUNDA OPCIÓN
############################################################################ INICIA TERCER OPCIÓN



    elif menu == 3:
        print("TOP 3 de estudiantes con las mejores notas promedio: ")

        
        averages = []

        
        for i in students_list:

            average_grade = (i["spanish_note"] + i["english_note"] + i["social_studies"] + i["science_note"]) / 4
            averages.append((i["name"], average_grade))

        # Ordenar los estudiantes por su promedio en orden descendente
        for i in range(len(averages)):
            for j in range(i + 1, len(averages)):
                if averages[i][1] < averages[j][1]:  # Comparar promedios
                    averages[i], averages[j] = averages[j], averages[i]  # Intercambiar

        # Imprimir los estudiantes con su promedio
        for name, avg in averages[:3]:
            print(f"Nombre: {name}, Promedio: {avg}")



############################################################################ FINALIZA TERCER OPCIÓN
############################################################################ INICIA CUARTA OPCIÓN



    elif menu == 4:
        print("Nota promedio entre las notas promedio: ")

        if not students_list:
            print("Debe registrar a los estudiantes primero ")

        else:

            # Calcular el promedio de los promedios
            averages = []

            for i in students_list:
                average_grade = sum([i["spanish_note"], i["english_note"], i["social_studies"], i["science_note"]]) / 4
                averages.append(average_grade)

            num_students = len(averages)  # Número total de estudiantes

            if num_students > 0:
                avg_all = sum(averages) / num_students  # Promedio de todos los promedios
                print(f"El promedio general de todos los estudiantes es: {avg_all}")
            else:
                print("No hay estudiantes para calcular el promedio.")



############################################################################ FINALIZA CUARTA OPCIÓN
############################################################################ INICIA QUINTA OPCIÓN



    elif menu == 5:
        if not students_list:
            print("Debe registrar a los estudiantes primero ")
        else:
            filename = "students.txt"
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Section", "Spanish", "English", "Social Studies", "Science"])
                for student in students_list:
                    writer.writerow([student["name"], student["section"], student["spanish_note"], student["english_note"], student["social_studies"], student["science_note"]])
            print(f"Datos exportados exitosamente a {filename}")



############################################################################ FINALIZA QUINTA OPCIÓN
############################################################################ INICIA SEXTA OPCIÓN



    elif menu == 6:
        filename = "students.txt"
        if not os.path.exists(filename): #Esto lo que hace es comprobar usando el "import os" para comrobar si el archivo especificado existe, usa True y False
            print("El archivo CSV con los datos no existe, exporte los datos primero ")
        with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                students_list = [
                    {
                        "name": row["Name"],
                        "section": row["Section"],
                        "spanish_note": float(row["Spanish"]),
                        "english_note": float(row["English"]),
                        "social_studies": float(row["Social Studies"]),
                        "science_note": float(row["Science"]),
                    }
                    for row in reader
                ]
                print("Datos importados exitosamente del archivo CSV.")    



############################################################################ FINALIZA SECTA OPCIÓN
############################################################################ INICIA SÉTIMA OPCIÓN



    elif menu == 7:
        print("Finalizó el programa")
        break

    else:
        print("Opción no válida")



############################################################################ FINALIZA SÉTIMA OPCIÓN

############################################################################ FIN PROGRAMA