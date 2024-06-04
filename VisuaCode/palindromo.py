palabra=input("intruduce la palabra: ")
nom=palabra.lower()
longitud=len(nom)
c=0
d=longitud-1
while c<longitud:
    if nom[c]==nom[d]:
        bandera=True
        c=c+1
        d=d-1
    else:
        bandera=False
        break
if bandera==True:
    print("es palindromo")
if bandera==False:
    print("no es palindromo")