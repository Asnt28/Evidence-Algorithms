Algoritmo sin_titulo
	Definir n1,suma,n2,res Como Entero
	Escribir "Ingresa numero 1"
	Leer n1
	Escribir "Ingresa numero 2"
	Leer n2
	suma = 0
	Mientras n1 > 0 Hacer
		suma=suma+(n1 mod 10)
		n1 = trunc(n1/10)
	Fin Mientras
	res=0
	Mientras n2 >0 Hacer
		res=res+(n2 mod 10)
		n2 = trunc(n2/10)
	Fin Mientras
	sum=suma+res
	escribir "La suma de los digitos es ", sum
FinAlgoritmo
