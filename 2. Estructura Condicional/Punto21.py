#21. Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo.
print("Hola usuario, ingrese un número entero de 4 digitos y determinaré si el segundo digito es igual al penúltimo.")
Numero=int(input("Ingresa el número por favor: "))
if Numero<=999 or Numero>=10000:
    print("El número ingresado no cumple con las condiciones especificadas.")
else:
    primerDigito=Numero//1000
    segundoDigito=(Numero//100)%10
    tercerDigito=(Numero//10)%10
    cuartoDigito=Numero%10

    if segundoDigito==tercerDigito:
        print("El segundo digito es igual al penúltimo digito")
    else:
        print("El segundo digito y el penúltimo no son iguales")