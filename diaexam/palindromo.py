
#Dias que llevas de vida apartir de tu fecha de nacimiento 

import texto.reordenar as reordenar
while True:
    texto=input("Humano por favor ingresa un palindromo:")
    esPalindromo=reordenar.palindromo(texto)
    if esPalindromo==True:
        print(f"Felicidades humano '{texto}' si es palindromo")
        break
    else:
        print(f"Humano tonto '{texto}' no es palindromo")