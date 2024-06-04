Algoritmo sin_titulo
	Definir n1,suma Como Entero
	Escribir "Ingresa numero 1"
	Leer n1
	suma = 0
	Mientras n1 > 0 Hacer
		suma=suma+(n1 mod 10)
		n1 = trunc(n1/10)
	Fin Mientras
	Si suma>30 Entonces
		Escribir "La suma de los digitos es mayor a 30"
		Escribir "La suma es " ,suma
	SiNo
		Escribir "La suma de los digitos es menor que 30"
		Escribir "La suma de los digitos es ", suma
	Fin Si
FinAlgoritmo
