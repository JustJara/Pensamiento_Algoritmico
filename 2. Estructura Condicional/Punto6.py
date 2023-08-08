# 6. Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
print("Hola usuario, ingrese un número entero de dos digitos para yo decirte si ambos digitos son iguales.")
Numero = int(input("Ingrese el número por favor: "))
if Numero<=9 or Numero>=100:
    print("El número no es válido, ingresa un número entero de 2 digitos")
else:
    primerNumero = int(Numero//10)
    segundoNumero = int(Numero%10)
    if primerNumero / segundoNumero==1:
        print("El primer digito es el mismo que el segundo")
    else:
        print("Los dos digitos son diferentes")