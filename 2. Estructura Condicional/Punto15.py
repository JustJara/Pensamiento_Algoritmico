#Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito.
mayor=0
print("Hola usuario, te pediré 3 números de dos digitos enteros y determinaré cuál es el mayor de los digitos")
Numero=int(input("Ingresa el primer número: "))
if Numero<=9 or Numero>=100:
    print("El número no cumple con las condiciones especificadas.")
else:
    if Numero>mayor:
        mayor = Numero
        Numero=int(input("Ingresa el segundo número: "))
    if Numero>mayor:
        mayor=Numero
        Numero=int(input("Ingresa el tercer número: "))
    if Numero>mayor:
        mayor=Numero
    print("El número mayor entre los 3 que ingresaste es:",mayor)