#28. Leer dos números enteros y determinar cuál es múltiplo de cuál.
print("Hola usuario, ingresa dos números enteros y determinaré cuál es múltiplo de cuál")
Numero1=int(input("Ingresa el primer número por favor: "))
Numero2=int(input("Ingresa el segundo número por favor: "))

if Numero1%Numero2==0:
    print("El primer número es múltiplo del segundo")
if Numero2%Numero1==0:
    print("El segundo número es múltiplo del primero")
if Numero1%Numero2!=0:
    print("El primer número no es múltiplo del segundo")
if Numero2%Numero1!=0:
    print("El segundo número no es múltiplo del primero")