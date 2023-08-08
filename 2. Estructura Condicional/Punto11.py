# 11. Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.
print("Hola usuario te pediré un número entero de 3 digitos para determinar cual de los digitos es mayor")
Numero= int(input("Ingresa el número por favor: "))
if Numero<=99 or Numero>=1000:
    print("El númreo no cumple con las condiciones especificadas.")
else:
    primerDigito= Numero//100
    segundoDigito= (Numero//10)%10
    tercerDigito= Numero%10

    if primerDigito>segundoDigito and primerDigito>tercerDigito:
        print("El primer digito es el mayor de los 3")
    elif segundoDigito>primerDigito and segundoDigito>tercerDigito:
        print("El segundo digito es el mayor de los 3")
    elif tercerDigito>primerDigito and tercerDigito>segundoDigito:
        print("El tercer digito es el mayor de los 3")