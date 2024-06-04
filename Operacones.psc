Algoritmo Operacones
	Definir opc,a,b,resultado como real
	opc = 10
	resultado = 0
	Mientras opc <> 0 Hacer
		Escribir "Ingresa tu primer valor"
		leer a
		Escribir "Ingresa tu segundo valor"
		leer b
		
		Escribir "¿Que oeracion deseas realizar?"
		Escribir "1 = Suma"
		Escribir "2 = Resta"
		Escribir "3 = Multiplicacion"
		Escribir "4 = Division"
		Escribir "5=  Cancelar"
		Escribir "Inserta el numero de la operacion que necesites"
		leer opc    
		Segun opc Hacer
			1:
				resultado = a+b
				Escribir "El resultado de la suma de los valores",a," + ",b," = ",resultado
			2:
				resultado = a-b
				Escribir "El resultado de la resta de los valores ",a," - ",b," = ",resultado
			3:
				resultado = a*b
				Escribir "El resultado de la multplicacion de los valores ",a," x ",b," = ",resultado
			4:
				resultado = a/b
				Escribir "El resultado de la divicion de los valores ",a," / ",b," = ",resultado
			De Otro Modo:
				Escribir "Opracion cancelada, hasta la vista baby"
				opc = 0
		Fin Segun  
	FinMientras
FinAlgoritmo
