Algoritmo nemero_mayor
	Definir n1,n2,n3 Como Real
	EScribir""
	Escribir "Determinar el numeromayor"
	Escribir Sin Saltar "Inserta el primer numero"
	Leer n1
	Escribir Sin Saltar "Ingresa elsegundo numero"
	leer n2
	Escribir Sin Saltar "Ingresa el tercer nuero"
	leer n3
	Escribir ""
	Si n1> n2 Y n1> n3 Entonces
		Escribir "El numero mayor es:" n1
	SiNo
		Si n2 > n1 Y n2 > n3 Entonces
			Escribir "Elnumero mayor es:" n2
		SiNo
			Escribir "El numero mayor es:" n3
		Fin Si
	Fin Si
FinAlgoritmo
