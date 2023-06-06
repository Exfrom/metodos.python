instructores = []

def agregar_instructor():
    nombre = input("Ingrese el nombre del instructor: ")
    instructores.append(nombre)
    print("Instructor agregado con éxito.")

def listar_instructores():
    if not instructores:
        print("No hay instructores en la lista.")
    else:
        print("Lista de instructores:")
        for instructor in instructores:
            print(instructor)

def modificar_instructor():
    if not instructores:
        print("No hay instructores en la lista.")
    else:
        nombre = input("Ingrese el nombre del instructor a modificar: ")
        encontrado = False
        for i in range(len(instructores)):
            if instructores[i].lower() == nombre.lower():
                nuevo_nombre = input("Ingrese el nuevo nombre del instructor: ")
                instructores[i] = nuevo_nombre
                encontrado = True
                print("Instructor modificado con éxito.")
                break
        if not encontrado:
            print("No se encontró el instructor en la lista.")

def borrar_instructor():
    if not instructores:
        print("No hay instructores en la lista.")
    else:
        nombre = input("Ingrese el nombre del instructor a borrar: ")
        encontrado = False
        for instructor in instructores:
            if instructor.lower() == nombre.lower():
                instructores.remove(instructor)
                encontrado = True
                print("Instructor borrado con éxito.")
                break
        if not encontrado:
            print("No se encontró el instructor en la lista.")

def buscar_instructor():
    if not instructores:
        print("No hay instructores en la lista.")
    else:
        nombre = input("Ingrese el nombre del instructor a buscar: ")
        encontrado = False
        for instructor in instructores:
            if instructor.lower() == nombre.lower():
                print("Instructor encontrado:", instructor)
                encontrado = True
                break
        if not encontrado:
            print("No se encontró el instructor en la lista.")

def ordenar_instructores():
    if not instructores:
        print("No hay instructores en la lista.")
    else:
        instructores.sort(key=lambda x: x.lower())
        print("Lista de instructores ordenada de A-Z:")
        for instructor in instructores:
            print(instructor)

while True:
    print("\n--- Menú de opciones ---")
    print("1. Agregar instructor")
    print("2. Listar instructores")
    print("3. Modificar instructor")
    print("4. Borrar instructor")
    print("5. Buscar instructor")
    print("6. Ordenar instructores")
    print("7. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        agregar_instructor()
    elif opcion == "2":
        listar_instructores()
    elif opcion == "3":
        modificar_instructor()
    elif opcion == "4":
        borrar_instructor()
    elif opcion == "5":
        buscar_instructor()
    elif opcion == "6":
        ordenar_instructores()
    elif opcion == "7":
        print("Hasta luego.")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 7.")