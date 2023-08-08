# Identificar si un número termina en 4
print("Hola usuario, dame un número para identificar si este termina en 4")
Numero = int(input("Ingresa el número: "))
if Numero %10==4:
    print("El número termina en 4")
else:
    print("El numero no termina en 4")