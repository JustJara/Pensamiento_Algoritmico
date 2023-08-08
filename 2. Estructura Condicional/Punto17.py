#Leer un número entero de tres dígitos y determinar cuántos dígitos pares tiene.
print("Ingrese un número entero de 3 digitos y determinaré cuántos digitos pares tiene")
Numero=int(input("Ingrese el número por favor: "))
if Numero<=99 or Numero>=1000:
    print("El número no cumple con las condiciones especificadas")
else:
    primerDigito=Numero//100
    segundoDigito=(Numero//10)%10
    tercerDigito=Numero%10

    if primerDigito%2==0:
        print("El primer digito es par")
    if segundoDigito%2==0:
        print("El segundo digito es par")
    else:
        print("El segundo digito no es par")
    if tercerDigito%2==0:
        print("el tercer digito es par")