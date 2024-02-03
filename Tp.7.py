class Alumnos:
    Alumnos_lista = []

    def __init__(self, Nombre = "", Apellido = "", Nacimiento = "", DNI = "", Notas = "", Faltas = "", Amonestaciones = ""):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Nacimiento = Nacimiento
        self.DNI = DNI
        self.Notas = Notas
        self.Faltas = Faltas
        self.Amonestaciones = Amonestaciones
    
    def insertar(self, alumno):
        self.Alumnos_lista.append(alumno)

    def eliminar(self, alumno):
        self.Alumnos_lista.remove(alumno)

    def CrearAlumnos(self):
        Juan = Alumnos("Juan","Manuel", "0/12/2003", "32322232", "21", "3232", "323")
        Pedro = Alumnos("Pedro", "Manuel", "0/12/2003","32322232", "21","3232","323")
        Luis = Alumnos("Luis", "Manuel", "0/12/2003","32322232", "21","3232","323")
        self.Alumnos_lista = [Juan,Pedro,Luis]

    def mostrarAlumnos(self):
        return self.Alumnos_lista

    def BuscarPorNombre(self, nombre):
        if len(self.Alumnos_lista) > 0:
            for alumno in self.Alumnos_lista:
                if (alumno.Nombre == nombre):
                    return alumno
            return None


    def Modificar(self, Caracteristica, Modificacion, nombre):
        alumno = self.BuscarPorNombre(nombre)
        self.Alumnos_lista.remove(alumno)
        if Caracteristica == "Nombre":
            alumno.Nombre = Modificacion
        elif Caracteristica == "Apellido":
            alumno.Apellido = Modificacion
        elif Caracteristica == "Nacimiento":
            alumno.Nacimiento = Modificacion
        elif Caracteristica == "DNI":
            alumno.DNI = Modificacion
        elif Caracteristica == "Notas":
            alumno.Notas = Modificacion
        elif Caracteristica == "Faltas":
            alumno.Faltas = Modificacion
        elif Caracteristica == "Amonestaciones":
            alumno.Amonestaciones = Modificacion
        self.Alumnos_lista.append(alumno)
        return alumno

instancia_alumno = Alumnos()
instancia_alumno.CrearAlumnos()
while True:
    Opcion = int(input("Que te gustaria hacer?\n" 
    "1 (Mostrar los datos de todos los alumnos\n"
    "2 (Buscar Alumnos por nombre)\n"
    "3 (Modificar sus datos)\n"
    "4 (Agregar un alumno)\n"
    "5 (Remover un alumno)\n"
    "6 (Salir) : " ))
    if Opcion == 1:
        todosalumnos = instancia_alumno.mostrarAlumnos()
        for alumno in todosalumnos:
            print(vars(alumno))
        pass
    elif Opcion == 2: 
        nombre = input('Ingrese el nombre: ')
        encontrado = instancia_alumno.BuscarPorNombre(nombre)
        if encontrado != None:
            print(vars(encontrado))
        else:
            print("No se encontro el alumno.")
    elif Opcion == 3:
        nombre = input("Que alumno quiere modificar? ")
        alumnomodificar = instancia_alumno.BuscarPorNombre(nombre)
        if alumnomodificar != None:
            print(vars(alumnomodificar))
            caracteristica = input("Que quiere modificar? ")
            modificacion = input(f"Ingrese el nuevo {caracteristica}: ")
            modificado  = instancia_alumno.Modificar(caracteristica,modificacion,nombre)
            print(vars(modificado))
        else:
            print("No se encontro el alumno")
    elif Opcion == 4:
        nombre = input("ingrese el nombre: ")
        apellido = input("Ingrese apellido: ")
        nacimiento = input("ingrese la fecha de nacimiento: ")
        dni = input("Ingrese el Dni: ")
        faltas = input("Ingrese la cantidad de faltas: ")
        notas = input("Ingrese las notas: ")
        amonestaciones = input("Ingrese la cantidad de amonestaciones")
        Nuevo = Alumnos(nombre,apellido,nacimiento,dni,faltas,notas,amonestaciones)
        instancia_alumno.insertar(Nuevo)
    elif Opcion == 5: 
        eliminar = (input("Que alumno quiere remover?: "))
        alumnoaeliminar = instancia_alumno.BuscarPorNombre(eliminar)
        if alumnoaeliminar != None:
            instancia_alumno.eliminar(alumnoaeliminar)
    elif Opcion == 6:
        break