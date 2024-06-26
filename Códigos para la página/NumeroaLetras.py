u = ["", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve"]
d = ["", "Diez", "Veinte", "Treinta", "Cuarenta", "Cincuenta", "Sesenta", "Setenta", "Ochenta", "Noventa"]
c = ["", "Cien", "Doscientos", "Trescientos", "Cuatrocientos", "Quinientos", "Seiscientos", "Setecientos", "Ochocientos", "Novecientos"]
 
def convertir(numero):
    if numero == 100: return "Cien"
    letra = c[numero // 100] + (d[(numero % 100) // 10] + " y ") * (numero % 100 > 20) + u[numero % 10]
    return letra.replace("Diez y", "Dieci").replace("Quince y", "Quince").replace("Veinte y", "Veinti")
 
numero = int(input("Ingrese un número entre 1 y 999: "))
print("Número en letras:", convertir(numero))
