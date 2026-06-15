import random

def juego_adivinanza():
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False
    print("Bienvenida al juego de adivinanzas de numeros" )
    print("Estoy pensando en un numero entre 1 y 100")

    while not adivinado:
        numero_introducido = int(input("Adivina el numero:"))
        intentos += 1

        if numero_introducido < numero_secreto:
            print("El numero correcto es mayor")
        elif numero_introducido > numero_secreto:
            print("El numero correcto es menor")
        else:
            adivinado = True
            print(f"Felicidades! Adivinaste el numero secreto en {intentos} intentos.")
juego_adivinanza()
