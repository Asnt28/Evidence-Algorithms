Algoritmo Dodecaedro 
	Escribir "Escribe la longitud de un lado del pentagono" 
	Leer s 
	Escribir "Pon la longitud de una arista:"
	Leer a
	Resultado <- (1/4)*(rc(5)*(5+2*(rc(5*s^2)))) 
	Area <- 12 * Resultado 
	AResultado <- 30 * s
	BResultado <- (15+7*rc(5)*a^3)/4
	Escribir "El resultado del area es:", Area 
	Escribir "El resultado del perimetro es:", AResultado
	Escribir "El resultado del volumen es:", BResultado
	
FinAlgoritmo
	