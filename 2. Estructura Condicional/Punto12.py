#12. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.
print("Hola usuario, ingrese un número entero de 3 digitos para determinar si alguno de los 3 digitos son multiplos del otro")
Numero = int(input("Ingrese el número por favor: "))
if Numero<=9 or Numero>=1000:
    print("El número no cumple con las condiciones especificadas")
else:
    primerDigito=Numero//100
    segundoDigito=(Numero//10)%10
    tercerDigito=Numero%10

    if primerDigito%segundoDigito==0:
        print("El primer digito es múltiplo del segundo digito")
    if primerDigito%tercerDigito==0:
        print("El primer digito es múltiplo del tercero")
    if segundoDigito%primerDigito==0:
        print("El segundo digito es múltiplo del primer digito")
    if segundoDigito%tercerDigito==0:
        print("El segundo digito es múltiplo del tercer digito")
    if tercerDigito%primerDigito==0:
        print("El tercer digito es múltiplo del primer digito")
    if tercerDigito%segundoDigito==0:
        print("El tercer digito es múltiplo del segundo")
    