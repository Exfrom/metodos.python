import random
##juego carisellazo

def main():
    print("Bienvenido al juego del Carisellazo")
    print("1.jugar: ")
    print("2.salir")
jugador = input("Ingrese el nombre del jugador: ")
def lanzarMoneda():
    if random.randint(0,1) == 0:
        print("Has ganado")
    else:
        print("Has perdido")
    



    #moneda = ["cara", "sello"]
    #resultado = random.choice(moneda)

    
