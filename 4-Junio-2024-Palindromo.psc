Algoritmo palindromo
	Definir a, b, c Como Entero
	Escribir "Dame una palabra"
	Leer palabra
	b = Longitud(palabra)
	a = 1
	c = 0
	Mientras a < b Hacer
		si Subcadena(palabra,a,a) <> Subcadena(palabra,b,b) entonces 
			c = c+1
		FinSi
		a = a + 1
		b = b - 1
	FinMientras
	si c = 0 Entonces
		Escribir "La palabra" ,  palabra, "es palindromo"
	SiNo
		Escribir "La palbra" ,  palabra, "no es palindromo"
	FinSi
	
FinAlgoritmo
