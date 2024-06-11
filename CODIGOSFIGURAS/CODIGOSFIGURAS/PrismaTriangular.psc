Algoritmo Prisma_triangular 
	Escribir "Escribe el primer lado" 
	Leer a 
	Escribir "Escribe el segundo lado"
	Leer b 
	Escribir "Escribe el tercer lado" 
	Leer c 
	Escribir "Escribe el semiperimetro"
	Leer s 
	Escribir "Escribe la altura"
	Leer h 
	AResultado<- rc(s)*(s-a)*(s-b)*(s-c)
	BResultado <-2 * AResultado 
	CResultado <-(a *h) + (b* h) + (c *h) 
	Area<- BResultado + CResultado 
	Perimetro<- a+b+c
	Areabase<-rc(s*(s-a)*(s-b)*(s-c))
	volumen<-Areabase*h
	Escribir "El resutado del area es:", Area 
	Escribir 'El resultado del perimetro es:', Perimetro
	Escribir 'El resultado del volumen es:', volumen 
FinAlgoritmo
