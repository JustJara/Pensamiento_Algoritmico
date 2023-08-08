#Leer un número entero y determinar si termina en 7.
print("Ingrese un número entero y determinaré si su último número termina en 7")
Numero=int(input("Ingrese el número por favor: "))
if Numero%10==7:
    print("El último digito termina en 7")
else:
    print("El último digito no termina en 7")