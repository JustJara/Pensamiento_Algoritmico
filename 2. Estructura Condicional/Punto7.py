# 7. Leer dos números enteros y determinar cuál es el mayor.
print("Hola usuario, ingresa un número de dos digitos para determinar cuál de los 2 digitos es mayor que el otro.")
Numero = int(input("Ingresa el número por favor: "))
if Numero<=9 or Numero>=100:
    print("El número no es válido, ingresa un número de solo dos digitos")
else:
    primerNumero= int(Numero//10)
    segundoNumero= int(Numero%10)
    if primerNumero>segundoNumero:
        print("El primer digito es mayor que el segundo")
    if primerNumero<segundoNumero:
        print("El primer digito es menor que el primero")
    if primerNumero==segundoNumero:
        print("Ambos números son iguales")