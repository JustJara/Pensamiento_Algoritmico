#Leer un número entero de tres dígitos y determinar si el primer dígito es igual al último.
print("Ingresa un número entero de 3 digitos para determinar si el primer digito es igual al último digito")
Numero=int(input("Ingresa el número por favor: "))
if Numero<=99 or Numero>=1000:
    print("Los números no cumplen con las condiciones especificadas anteriormente")
else:
    primerDigito=Numero//100
    segundoDigito=(Numero//10)%10
    tercerDigito=Numero%10

    if primerDigito==tercerDigito:
        print("El primer y tercer digito son iguales")
    else:
        print("El primer y tercer digito son diferentes")