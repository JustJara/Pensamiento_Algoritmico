#Leer un número entero de 4 dígitos y determinar si el primer dígito es múltiplo de alguno de los otros dígitos.
print("Hola usuario, ingrese un número entero de 4 digitos y determinaré si el primer digito es múltiplo de alguno de los otros.")
Numero=int(input("Ingrese el número por favor: "))
if Numero<=999 or Numero>=10000:
    print("El número ingresado no es válido.")
else:

    primerDigito=Numero//1000
    segundoDigito=(Numero//100)%10
    tercerDigito=(Numero//10)%10
    cuartoDigito=Numero%10

    if primerDigito%segundoDigito==0:
        print("El primer digito es múltiplo del segundo")
    if primerDigito%tercerDigito==0:
        print("El primer digito es múltiplo del tercer digito")
    if primerDigito%cuartoDigito==0:
        print("El primer digito es múltiplo del cuarto digito")
    if primerDigito%segundoDigito!=0 and primerDigito%tercerDigito!=0 and primerDigito%cuartoDigito!=0:
        print("Ningún digito es múltiplo del primero")