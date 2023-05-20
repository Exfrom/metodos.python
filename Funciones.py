#1. Declaracion de un metodo
def suma(n1,n2):
    #cuerpo metodo
    suma = num1+num2
    return suma
#2. Declaracion del metodo con parametros
def restar(n1,n2):
    #cuerpo del metodo
    restar=n1-n2
    print(f"La resta entre ${n1} y ${n2} es {restar}")
#3 Declaracion metodo con valor de retorno
def multiplicar(n1,n2):
    #cuerpo del metodo
    multiplicar=n1,n2
    #retorno del dato
    return multiplicar

#metodo promedio  
def sumap():
    #cuerpo del metodo
    seguir="si"
    suma=0
    cant=0
    while seguir=="si":
        numero=int(input("Digite el numero entero: "))
        suma=suma+numero
        cant=cant+1
        seguir=input("Para seguir digite si de lo contrario no: ")
    return (suma,cant)

num1=int(input("Ingrese el numero 1: "))
num2=int(input("Ingrese el numero 2: "))

#llamado o invocacion del metodo

print("Menu opciones")
op=input("Ingrese la opcion segun la operacion a realizar: \n 1.suma 2.Resta 3.Multiplicar 4.Division 5.promedio 6.promedodevariosnumeros: ")
if op=="1":
    #Invocar el metodo
    suma()
elif op=="2":
    restar(num1,num2)

elif op=="3":
    #Invocar metodo con valor de retorno
    multiplicar(num1,num2)
    print(f"la multiplicacion entre {num1} y {num2} es {multiplicar(num1,num2)}")
    #guardar una variable para operarlo en otro momento
    producto=multiplicar(num1,num2)
    if producto<50:
        print("EL producto es menor que 50")
    else:
        print("El producto es mayor que 50")

elif op=="5":
    #se debe utilizar el metodo suma para calcular el promedio
    suma(num1,num2)
    promedio=suma(num1,num2)/2
elif op=="6":
    a,b=sumap()
    promedio=a/b
    print(f"El promedio de los valores ingresados es {promedio}")
else:
    print("opcion invalida")