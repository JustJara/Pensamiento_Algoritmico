#Leer un número entero y determinar si tiene 3 dígitos.
print("Hola usuario, dame un numero para yo identificar si este tiene 3 digitos")
Numero = float(input("Ingrese el número: "))
if(Numero>99 and Numero<1000) or (Numero > -99 and Numero < -1000):
    print("Su numero tiene 3 digitos")
elif( Numero < 100):
    print("Su numero tiene 2 digitos")
if(Numero>999):
    print("Su numero tiene 3 digitos o más")