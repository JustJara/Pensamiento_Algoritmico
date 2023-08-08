#29. Leer tres números enteros y determinar si el último dígito de los tres números es igual.
print("Hola usuario, ingrese 3 números enteros y determinaré si el último digito de los 3 es igual.")
Numero1=int(input("Ingrese el primer número por favor: "))
Numero2=int(input("Ingrese el segundo número por favor: "))
Numero3=int(input("Ingrese el tercer número por favor: "))

tercerDigito1=Numero1%10
tercerDigito2=Numero2%10
tercerDigito3=Numero3%10

if tercerDigito1 == tercerDigito2 ==tercerDigito3:
    print("Los últimos 3 digitos de los números ingresados son iguales")
else:
    print("Los 3 últimos digitos de los números que ingresaste no son inguales.")