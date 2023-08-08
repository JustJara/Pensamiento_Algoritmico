# 9. Leer dos números enteros de dos dígitos y determinar si la suma de los dos números origina un número par
print("Hola usuario, cuando ingreses dos números yo haré una suma entre ellos y determinaré si el resultado es un número par")
primerNumero = int(input("Ingrese el primer número de 2 digitos por favor."))
segundoNumero= int(input("Ingrese el segundo número de 2 digitos por favor"))
if primerNumero<=9 or primerNumero>=100 or segundoNumero<=9 or segundoNumero>=100:
    print("Ingrese números con las condiciones anteriormente mencionadas.")
else:
    sumatoria = primerNumero+segundoNumero
    if sumatoria%2==0:
        print("La suma de",primerNumero," y ",segundoNumero," es ",sumatoria, "Y este número es par" )
    else: 
        print("La sumatoria de los dos números no es par")