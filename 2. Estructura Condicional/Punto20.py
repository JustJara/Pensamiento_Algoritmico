#20. Leer un número entero de cinco dígitos y determinar si es un número capicúa. Ej. 15651,59895.
print("Hola usuario, ingresa un número entero de 5 digitos para determinar si es un número capicúa.")
Numero=int(input("Ingresa el número por favor: "))
if Numero<10000 or Numero>99999:
    print("El número ingresado no cumple con las condiciones especificadas")
else:
    primerDigito=Numero//10000
    segundoDigito=(Numero//1000)%10
    cuartoDigito=(Numero//10)%10
    quintoDigito=Numero%10

    if primerDigito==quintoDigito and segundoDigito==cuartoDigito:
        print("El número ingresado es capicúa.")
    else:
        print("El número no es capicúa.")