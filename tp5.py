# 1) Hacer un programa que gestiones datos para una escuela.
# El programa tiene que ser capaz de:
# a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre,
# Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las
# notas, cantidad de faltas, cantidad de amonestaciones recibidas.
# b) Mostrar los datos de cada alumno
# c) Modificar los datos de los alumnos
# d) Agregar alumnos
# e) Expulsar alumnos
def ParametrosAlumno (NumeroDeLista):
   diccionario_principal[NumeroDeLista] = {
        "Nombre": "",
        "Apellido": "",
        "Nacimiento": "",
        "DNI": "",
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
diccionario_principal = {1 : {"Nombre" : "Juan", "Apellido" : "Medina", "Nacimiento" : "7/12/2003", "DNI" : 32325276, "Notas" : [5,6,7,2,8,9], "Faltas" : 7, "Amonestaciones" : 3}}
while True:
    Opcion = int(input("Que te gustaria hacer?\n" 
    "1 (Mostrar sus datos\n"
    "2 (Mostrar un dato especifico)\n"
    "3 (Modificar sus datos)\n"
    "4 (Agregar un alumno)\n"
    "5 (Remover un alumno)\n"
    "6 (Salir) : " ))
    if Opcion == 1:
        Numero_de_Alumno = int(input("Cual dato de alumno te interesa? (Por numero de lista)"))
        print(diccionario_principal[Numero_de_Alumno])
        pass
    elif Opcion == 2: 
        print ("Cual alumno quiere ver?: ")
        Numero_de_Alumno = int(input())
        print ("Que desea ver: \n"
               "Nombre-Apellido-Nacimiento-DNI-Nacimiento-Notas-Faltas-Amonestaciones: ")
        Caracteristicas = (input())
        print(diccionario_principal[Numero_de_Alumno][Caracteristicas])
    elif Opcion == 3:
        Numero_de_Alumno = int(input("Cual alumno te interesa modificar? (Por numero de lista): "))
        while True:
            Caracteristicas = (input("Que desea cambiar: \n"
               "Nombre-Apellido-Nacimiento-DNI-Nacimiento-Notas-Faltas-Amonestaciones: "))
            Modificacion = input(f"Escriba su nuevo {Caracteristicas}: ")
            diccionario_principal[Numero_de_Alumno][Caracteristicas] = Modificacion
            salir = input("Quieres seguir modificando? sino escriba Salir: ")
            if "Salir" == salir:
                break
        pass
    elif Opcion == 4:
        Alumno = int(input("Ponga el numero de lista del alumno: "))
        ParametrosAlumno(Alumno)
        print("Para modificar sus datos use la funcion 3")
        pass
    elif Opcion == 5: 
        Numero_de_Alumno = int(input("Que alumno quiere remover?: "))
        del diccionario_principal[Numero_de_Alumno]
    elif Opcion == 6:
        break



