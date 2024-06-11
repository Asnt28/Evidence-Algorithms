Algoritmo TrianguloObtusangulo
	Escribir 'un lado:'
	Leer a
	Escribir 'un lado:'
	Leer b
	Escribir 'un lado:'
	Leer c
	s<- (a+b+c)/2
	Resultado<- rc(s*(s-a)*(s-b)*(s-c))
	Perimetro<- a+b+c
	Escribir 'El resultado del area es:', Resultado
	Escribir 'El resultado del perimetro es:', Perimetro
FinAlgoritmo