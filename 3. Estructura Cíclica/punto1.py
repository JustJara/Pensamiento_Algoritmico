"""
Leer un número entero de dos dígitos menor que 20 y determinar si es primo
"""

print("Hola usuario digita un número entero de dos digitos que sea menor a 20 para determinar si es primo")
numero = int(input("Ingresa el número por favor: "))
if numero < 10 or numero >20:
    print("El número que ingresaste no cumple con las condiciones especificadas")
else:
    contadorDivisores=0
    for i in range(1,numero,1):
        if numero%i==0:
            contadorDivisores= contadorDivisores+1
    if contadorDivisores >= 3:
        print("El número NO es primo")
    elif contadorDivisores <=2:
        print("El número es primo")