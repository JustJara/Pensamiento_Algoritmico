#13. Leer tres números enteros y determinar cuál es el mayor. Usar solamente dos variables.
mayor = 0
print("Te pediré 3 números para determinar cuál es mayor")

Numero=int(input("Ingrese el primer número: "))
if Numero > mayor:
    mayor = Numero
Numero=int(input("Ingrese el segundo número: "))
if Numero > mayor:
    mayor = Numero
Numero=int(input("Ingresa el tercer número"))
if Numero > mayor:
    mayor = Numero
print("El número mayor es: ",mayor)