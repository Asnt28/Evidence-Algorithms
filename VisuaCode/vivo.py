
from datetime import datetime
def dias_vivo(fecha_nacimiento):
    hoy = datetime.now()
    nacimiento = datetime.strptime
    (fecha_nacimiento, "%d-%m-%y")
    dias_vivo = (hoy-nacimiento).days
    return dias_vivo
tu_fecha = input("Introduce tufecha de nacimiento (DIA-MES-AÑO):")
dias = dias_vivo(tu_fecha)
print(f"Llevas {dias} vivo")