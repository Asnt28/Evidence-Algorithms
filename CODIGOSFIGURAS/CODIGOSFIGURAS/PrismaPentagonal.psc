Algoritmo Prisma_Pentagonal 
	Escribir "Escribe la longitud de uno de los lados del Pentagono" 
	Leer s 
	Escribir "Escribe la altura" 
	Leer h 
	AResultado<- (1/4)*(rc(5)*(5+2*rc(5)*s^2)) 
	BResultado<- 2* AResultado
	CResultado<-5*s*h 
	Area <-(2*AResultado)+CResultado
	Perimetro<-5*s
	Areabase<- (1/4)*rc(5*(5+2*rc(5)))*s^2
	volumen<-(1/3)*Areabase*h
	Escribir "El resutado del area es:", Area 
	Escribir 'El resultado del perimetro es:', Perimetro
	Escribir 'El resultado del volumen es:', volumen 
FinAlgoritmo
