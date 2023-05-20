import random
saldoinicial = 1000  
jugador = input("Ingrese el nombre del jugador:  ")   
def lanzarMoneda():
    moneda=["cara", "sello"]
    resultado = random.choice(moneda)
    return resultado

def ganar():
    global saldoinicial
    saldoinicial = saldoinicial + 1000
    print("Has ganado")

