import random
 
def juego_ppt(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"
 
def main():
    opciones = ["piedra", "papel", "tijera"]
     
    while True:
        jugador = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
         
        if jugador == "salir":
            print("¡Hasta luego!")
            break
         
        if jugador not in opciones:
            print("Opción inválida. Inténtalo de nuevo.")
            continue
         
        computadora = random.choice(opciones)
         
        resultado = juego_ppt(jugador, computadora)
         
        print(f"Computadora eligió: {computadora}")
        print(f"Tú {resultado}.")
 
if __name__ == "__main__":
    main()