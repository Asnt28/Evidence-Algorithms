from datetime import datetime
 
def calcular_edad():
    try:
        nacimiento = input("Ingrese su fecha de nacimiento (AAAA-MM-DD): ")
        fecha_nacimiento = datetime.strptime(nacimiento, '%Y-%m-%d')
        fecha_actual = datetime.now()
 
        edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
         
        print(f"Tu edad es: {edad} años")
    except ValueError:
        print("Formato de fecha incorrecto")
 
calcular_edad()
