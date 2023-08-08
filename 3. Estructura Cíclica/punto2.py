# Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos.

print("Ingresa un número entedor de dos digitos y yo determinaré si sus digitos son primos.")
num = int(input("Ingrese el número por favor: "))
if num<10 or num>99:
    print("El número que ingresaste no cumple con las condiciones especificada.")
else:
    contadorDivisores1= 0
    contadorDivisores2= 0
    primerDigito= num//10
    segundoDigito= num%10

    for i in range (1,primerDigito+1,1):
        if primerDigito%i==0:
            contadorDivisores1 = contadorDivisores1 + 1

    if contadorDivisores1>=3:
        print("El primer digito no es primo")
    elif contadorDivisores1<=2:
        print("El primer digito es primo")

    for j in range (1,segundoDigito+1,1):
        if segundoDigito%j==0:
            contadorDivisores2 = contadorDivisores2 + 1
    if contadorDivisores2>=3:
        print("El primer digito no es primo")
    elif contadorDivisores2<=2:
        print("El primer digito es primo")
    
    