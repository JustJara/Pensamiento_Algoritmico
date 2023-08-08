#27. Leer un número entero de 4 dígitos y determinar si tiene más dígitos pares o impares.
print("Hola usuario, ingrese un número entero de 4 digitos y yo determinaré si tiene más digitos pares o impares")
Numero=int(input("Ingrese el número por favor: "))
if Numero<=999 or Numero>=10000:
    print("El número ingresado no cumple con las condiciones especificadas.")
else:

    primerDigito=Numero//1000
    segundoDigito=(Numero//100)%10
    tercerDigito=(Numero//10)%10
    cuartoDigito=Numero%10
    pares=0
    impares=0

    if primerDigito%2==0:
        pares=pares+1
    else:
        impares=impares+1
    if segundoDigito%2==0:
        pares=pares+1
    else:
        impares=impares+1
    if tercerDigito%2==0:
        pares=pares+1
    else:
        impares=impares+1
    if cuartoDigito%2==0:
        pares=pares+1
    else:
        impares=impares+1
    if pares>impares:
        print("Hay más números pares que impares")
    elif impares>pares:
        print("Hay más números impares que pares")
    elif pares==impares:
        print("Hay la misma cantidad de digitos pares que impares")