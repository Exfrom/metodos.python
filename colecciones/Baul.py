baul=[]

while True:
    print("opciones")
    print("1. Agregar un articulo al baul")
    print("2. Listar los articulos al baul")
    print("3. Borrar el último elemento del baul")
    print("4. Borrar un artículo del baul")
    print("5. Salir")
    opcion = input("seleccione una opcion:")

    if opcion == "1":
        articulo = input("Ingrese el nombre del articulo: ")
        baul.append(articulo)
        print(f"El articulo: {articulo} ha sido agregado al baul.")
    elif opcion == "2":
        if len(baul) == 0:
            print("El baul está vacío.")
        else:
            print("Artículos del baul:")
            for p, articulo in enumerate(sorted(baul)):
                print(f"{p+1}. {articulo}")

    elif opcion == "3":
        if len(baul) == 0:
            print("El baul está vacío.")
        else:
            articulo_borrado = baul.pop()
            print(f"{articulo_borrado} ha sido borrado del baul.")
    
    elif opcion == "4":
        if len(baul) == 0:
            print("El baul está vacío.")
        else:
            print("Artículos en el baul:")
            for i, articulo in enumerate(baul):
                print(f"{i}: {articulo}")
            
            index = input("Ingrese el número del artículo que desea borrar: ")
            try:
                index = int(index)
                articulo_borrado = baul.pop(index)
                print(f"{articulo_borrado} ha sido borrado del baul.")
            except ValueError:
                print("Por favor ingrese un número válido.")
            except IndexError:
                print("Por favor ingrese un número de artículo válido.")
    elif opcion == "5":
        
        print("Saliendo del programa...")
        break
    
    else:
        print("Por favor seleccione una opción válida.")