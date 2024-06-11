from datetime import datetime

def dias_vivo (fecha_nacimiento):
    hoy = datetime.now()
    nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
    dias_vivo =  (hoy-nacimiento).days
    return dias_vivo
tu_fecha = input ("Ingresa tu fecha de nacimiento con formato (DIA-MES-AÑO): ")
dias = dias_vivo (tu_fecha) 
print(f"Tu llevas estos dias vivo: {dias}")



