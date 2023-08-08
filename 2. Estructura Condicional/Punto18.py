#18. Leer un número entero de tres dígitos y determinar si alguno de sus dígitos es igual a la suma de los otros dos.
print("Ingrese un número entero de 3 digitos y determinaré si algunos digitos es igual a la suma de los otros")
Numero= int(input("Ingrese el número por favor: "))
if Numero<=99 or Numero>=1000:
    print("El número no cumple con las condiciones especificadas.")
else:
    primerDigito=Numero//100
    segundoDigito=(Numero//10)%10
    tercerDigito=Numero%10

    if primerDigito+segundoDigito==tercerDigito:
        print("El tercer digito es igual a la sumatoria del primer digito con el segundo digito")
    elif segundoDigito+tercerDigito==primerDigito:
        print("El primer digito es igual a la sumatoria de el segundo digito con el tercero")
    elif primerDigito+tercerDigito==segundoDigito:
        print("El segundo digito es igual a la sumatoria de el primer digito con el tercer digito")
    elif primerDigito+segundoDigito!=tercerDigito or segundoDigito+tercerDigito!=primerDigito or primerDigito+tercerDigito!=segundoDigito:
        print("Ninguno de los digitos ingresado es la sumatoria de los demás")