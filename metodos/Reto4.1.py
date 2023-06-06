import random

saldo_global = 1000  # Saldo inicial o global

def lanzar_moneda():
    #Lanza una moneda y devuelve el resultado: cara o sello.
    opciones = ["cara", "sello"]
    resultado = random.choice(opciones)
    return resultado

def ganar(monto, saldo):
    #Aumenta el saldo del jugador al doble de la apuesta y muestra un mensaje de victoria.
    saldo += monto * 2
    print("¡Has ganado!", monto, "doblado. Saldo actual:", saldo)
    return saldo

def perder(monto, saldo):
    #Reduce el saldo del jugador en el valor de la apuesta y muestra un mensaje de derrota.
    saldo -= monto
    print("Has perdido.", monto, "deducido. Saldo actual:", saldo)
    return saldo

def jugar():
    #Permite al jugador elegir cara o sello y apostar un monto.
    jugador = input("Ingrese el nombre del jugador: ")
    saldo = saldo_global
    while True:
        print("Saldo actual:", saldo)
        opcion = input("Elige cara o sello: ")
        monto_apuesta = int(input("Ingrese el monto de la apuesta: "))
        resultado = lanzar_moneda()
        if resultado == opcion:
            saldo = ganar(monto_apuesta, saldo)
        else:
            saldo = perder(monto_apuesta, saldo)

        continuar = input("¿Deseas continuar jugando? (s/n): ")
        if continuar.lower() != "s":
            break

    print("Juego terminado. ¡Gracias por jugar,", jugador + "! Tu saldo final es:", saldo)

# Ejecutar el juego
jugar()
