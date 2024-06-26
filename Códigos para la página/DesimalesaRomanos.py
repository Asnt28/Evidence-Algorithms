def decimal_a_romano(num):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = ""
    i = 0
 
    while num > 0:
        div = num // valores[i]
        num %= valores[i]
        resultado += simbolos[i] * div
        i += 1
 
    return resultado
 
numero_decimal = int(input("Ingresa un número decimal: "))
numero_romano = decimal_a_romano(numero_decimal)
print(f"El número romano correspondiente es: {numero_romano}")