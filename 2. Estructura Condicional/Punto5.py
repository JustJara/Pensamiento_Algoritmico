# Leer un número entero de dos dígitos y determinar si un dígito es múltiplo del otro
print(" Hola usuario, dame un número de dos digitos y te diré si ellos dos son múltiplos del otro")
Numero = int(input("Ingresa el número por favor: "))
if Numero<=9 or Numero>=100:
    print("El número no es válido, ingrese un número de dos digitos")
segundoDigito = int(Numero%10)
primerDigito = int(Numero//10)

if primerDigito%segundoDigito==0:
    print("El primer digito es múltiplo del segundo")
else:
    print("EL primer digito no es múltiplo del segundo")
if segundoDigito%primerDigito==0:
    print("El segundo digito es múltiplo del primero")
else:
    print("El segundo digito no es múltiplo del primero")