# Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
print("Hola usuario, ingresa un número de dos digitos para yo identificar si ambos son pares")
Numero = int(input("Ingrese el número por favor: "))
if Numero<=9 or Numero>=100:
    print("Número no válido, ingrese un número entero de DOS digitos")
else:
    segundoDigito = int(Numero%10)
    primerDigito = int(Numero//10)
if primerDigito %2 == 0:
        print("el primer digito es par")
else:
        print("el primer digito no es par")
if segundoDigito %2 == 0:
    print("el segundo digito es par")
else:
    print ("el segundo digito no es par")