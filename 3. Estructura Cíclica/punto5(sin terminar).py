"""
Leer un número entero de 2 dígitos y si es par mostrar en pantalla la suma de sus dígitos, 
si es primo y mayor que 50 mostrar en pantalla su último dígito y si es múltiplo de 5 y 
menor que 30 mostrar en pantalla el primer dígito.
"""

print("Hola usuario ingresa un número entero de dos digitos, si es par te mostraré la suma de sus digitos, si es primo y menor a 10 te mostraré el último digito y si es mútiplo de 5 y menor que 30 mostraré el primer digito.")

num = int(input("Ingresa el número por favor: "))
if num>99 or num<10:
    contadorDivisores= 0
    for i in range(1,num,1):
        if num%i==0:
            contadorDivisores= contadorDivisores+1
    if num%2==0:
        primerDigito= num//10
        segundoDigito= num%10
        suma= primerDigito+segundoDigito
        print("Como el número es par entonces la suma de sus digitos es: ",suma)
    if contadorDivisores<=2 and