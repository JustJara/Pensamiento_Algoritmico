#26. Leer un número entero de dos dígitos, guardar cada dígito en una variable diferente y luego mostrarlas en pantalla.
print("Hola usuario, ingrese un número entero de dos digitos y yo le mostraré cada uno de sus digitos por separado")
Numero=int(input("Ingrese el número por favor: "))
if Numero<=9 or Numero>=100:
    print("El número ingresado no es válido.")
else:
    primerDigito=Numero//10
    segundoDigito=Numero%10

    print("El primer digito es: ",primerDigito,"y el segundo digito es: ",segundoDigito)