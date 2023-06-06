
instructores = []

while True:
    print("Elija una opción:")
    print("1. Agregar un instructor")
    print("2. Listar los instructores")
    print("3. Modificar un instructor")
    print("4. Borrar un instructor")
    print("5. Buscar un instructor por nombre")
    print("6. Ordenar la lista de instructores")
    print("7. Salir")
    
    opcion = input("Opción seleccionada: ")
    
    if opcion == "1":
        
        nombre = input("Ingrese el nombre del instructor: ")
        instructores.append(nombre)
        print("El instructor", nombre, "ha sido agregado a la lista.")
    elif opcion == "2":
        if len(instructores) > 0:
            print("Lista de instructores:")
            for l, instructor in enumerate(sorted(instructores)):
                print(f"{l+1}. {instructor}")
        else:
            print("La lista de instructores está vacía.")
    elif opcion == "3":
       
        index = int(input("Ingrese el índice del instructor a modificar: "))
        if index >= 0 and index < len(instructores):
            nombre = input("Ingrese el nuevo nombre del instructor: ")
            instructores[index] = nombre
            print("El instructor ha sido modificado.")
        else:
            print("El índice ingresado es inválido.")
    elif opcion == "4":
        
        index = int(input("Ingrese el índice del instructor a borrar: "))
        if index >= 0 and index < len(instructores):
            nombre = instructores.pop(index)
            print("El instructor", nombre, "ha sido borrado de la lista.")
        else:
            print("El índice ingresado es inválido.")
    elif opcion == "5":
       
        nombre = input("Ingrese el nombre del instructor a buscar: ").lower()
        encontrado = False
        for instructor in instructores:
            if instructor.lower() == nombre:
                print("El instructor", instructor, "fue encontrado.")
                encontrado = True
                break
        if not encontrado:
            print("El instructor no fue encontrado.")
    elif opcion == "6":
        instructores_ordenados = sorted(instructores)
        print("Lista de instructores ordenada alfabéticamente A-Z:")
        for l, instructor in enumerate(instructores_ordenados):
            print(f"{l+1}. {instructor}")
    elif opcion == "7":
        
        print("Saliendo del programa... Adios!")
        break
    else:
        print("Opción inválida. Por favor ingrese una opción del 1 al 7.")
       








