#definicion o declaracion de la lista
numeros=[1,2,3,4]
#Mostrar contenido integro de la lista
print(numeros)
#Mostrar posicion particular
print(numeros[2])
#Mostrar ultima posicion de la lista
print(numeros[-1])
#Modificar el valor de un elemento en la lista
numeros[1]=9
print(numeros)
#Recorrer elementos de la lista
for p in numeros:
    print(p)
#Recorrer posicion por posicion accediente tanto al index como al elemento lista
for i,e in enumerate(numeros):
    #print(i,e)
    print("En la posicion" ,i, "se encuentra el elemento:" ,e)


generos=["Jazz", "Salsa", "Rock"]
#recorrer dos listas al mismo tiempo
for l1,l2 in zip(numeros, generos):
    print(l1,l2)
#Obtener la longitud de la lista
print(len(generos))