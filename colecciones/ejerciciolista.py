comida=["combo", "hamburguesa", "Pizza"]
#anadir elemento
comida.append("gaseosa")
print(comida)
#agregar varios elementos
comida.extend(["malteada", "perro caliente"])
print(comida)
#longitud de la lista
print(len(comida))
#
comida.sort()
print(comida)
#comida.insert(2,"empanada")

for p, e in enumerate(comida):
    print("En la posicion" ,p, "Se encuentra el elemento" ,e)
#insertar elemento
comida.insert(2,"empanada")
print(comida)

comida.reverse()
comida.sort(reverse=True)
#borrar elementode la lista
comida.remove("gaseosa")
print(comida)
#borrar un elemento de una posicion especifica
del comida[4]
print(comida)
#borrar el ultimo elemento de la lista
comida.pop()
print(comida)
#devolver en que posicion esta un elemento de la lista
print(comida.index("malteada"))