Algoritmo Piramide_Triangular
	Escribir "Escribe el semiperimetro" 
	Leer s 
	Escribir "Escribe la altura" 
	Leer h
	Escribir "Escribe la base" 
	Leer b 
	AResultado<- rc(s)*(s-a)*(s-b)*(s-c) 
	BResultado<-1/2*b*h
	Area<- AResultado+BResultado 
	Perimetro<- 3*s
	Areabase <-(rc(3)/4)*s^2
	volumen<-(1/3)*Areabase*h
	Escribir "El resutado del area es:", Area 
	Escribir 'El resultado del perimetro es:', Perimetro
	Escribir 'El resultado del volumen es:', volumen 
FinAlgoritmo
