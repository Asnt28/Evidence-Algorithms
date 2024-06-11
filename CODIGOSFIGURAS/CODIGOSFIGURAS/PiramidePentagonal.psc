Algoritmo Piramide_Pentagonal
	Escribir "Escribe el semiperimetro"
	Leer s 
	Escribir "Escribe la base" 
	Leer b
	Escribir "Escribe la altura" 
	Leer h 
	Escribir "Escribe una logngitud del pentagono"
	Leer s
	AResultado <-(1/4)*(rc(5)*(5+2*rc(5)*s^2))
	BResultado<-(1/2)*b*h 
	Area <-AResultado+5*(BResultado) 
	Perimetro<- 5*s
	Areabase<- (1/4)*rc(5*(5+2*rc(5)*s^2))
	volumen<-(1/3)*Areabase*h
	Escribir "El resutado del area es:", Area 
	Escribir 'El resultado del perimetro es:', Perimetro
	Escribir 'El resultado del volumen es:', volumen 
FinAlgoritmo
	