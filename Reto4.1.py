import random
saldo = 1000  
    
def lanzarMoneda():
    jugador = input("Ingresa el nombre del jugador: ")
    resultado = random.choice(["cara", "sello"])
    return resultado

    
    
