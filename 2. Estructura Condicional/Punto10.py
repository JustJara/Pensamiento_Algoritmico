#10. Leer un número entero de tres dígitos y determinar si al menos dos de sus tres dígitos son iguales.
print("Hola usuario, dame un número entero de 3 digitos y yo determinaré si alguno de los 3 digitos son iguales")
Numero=int(input("Ingrese el número de 3 digitos entero por favor: "))
if Numero <=100 or Numero>=1000:
    print("El número no cumple con las condiciones especificadas")
else:
    primerDigito= Numero//100
    segundoDigito= (Numero//10)%10
    tercerDigito= Numero%10
    print("El primer digito es", primerDigito,", el segundo digito es",segundoDigito," y el tercer digito es",tercerDigito,)

    if primerDigito == segundoDigito == tercerDigito:
        print("Los 3 digitos son iguales")
    if primerDigito == segundoDigito or segundoDigito == primerDigito:
        print("El primer digito es igual al segundo digito")
    if primerDigito == tercerDigito or tercerDigito == primerDigito:
        print("El primer digito es igual al tercer digito")
    if segundoDigito == tercerDigito:
        print("El segundo digito es igual al tercero")