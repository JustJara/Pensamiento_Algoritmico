# Identificar si un número dado es positivo o negativo
print("Hola usuario, si me das un número te diré si este es negativo o positivo")
n = float(input("Ingrese el numero por favor: "))
if n < 0:
    print("Su número es negativo")
elif n>0:
    print("Su número es positivo")