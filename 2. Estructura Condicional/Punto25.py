#25. Leer un número entero menor que mil y determinar cuantos dígitos tiene.
print("Hola usuario, ingrese un número entero menor a mil y yo determinaré cuántos digitos tiene")
Numero=int(input("Ingrese el número por favor: "))
if Numero>1000:
    print("El número no cumple con las condiciones especificadas.")
else:
    if Numero<10:
        print("El número tiene 1 solo digito")
    if Numero<100 and Numero>=10:
        print("El número tiene 2 digitos.")
    if Numero<1000 and Numero>=100:
        print("El número tiene 3 digitos")
    