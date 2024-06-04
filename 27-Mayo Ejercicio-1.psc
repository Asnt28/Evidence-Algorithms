Algoritmo sin_titulo
	Definir n1,suma Como Entero
	Escribir "Ingresa numero 1"
	Leer n1
	suma = 0
	Mientras n1 > 0 Hacer
		suma=suma+(n1 mod 10)
		n1 = trunc(n1/10)
	Fin Mientras
	Escribir ""
	Si suma mod 3=0 Entonces
		Escribir "Si es multiplo de 3 el numero ", suma
	SiNo
		Escribir "No es multiplo de 3 el numero ", suma
	Fin Si
FinAlgoritmo
