Algoritmo Piramide_Rectangular 
	Escribir "Escribe la longitud" 
	Leer lg 
	Escribir "Escribe la anchura" 
	Leer an 
	Escribir "Escribe la base"
	Leer b
	Escribir "Escribe la altura" 
	Leer h 
	AResultado<-lg* an 
	BResultado<-1/2*b*h 
	Area<-AResultado+BResultado 
	Perimetro<- 2*(lg+an)
	Areabase <-lg*an
	volumen<- (1/3)*Areabase*h
	Escribir "El resutado del area es:", Area 
	Escribir 'El resultado del perimetro es:', Perimetro
	Escribir 'El resultado del volumen es:', volumen 
FinAlgoritmo

