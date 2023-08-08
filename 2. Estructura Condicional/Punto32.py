#32. Leer dos números enteros y determinar si la diferencia entre los dos es un número divisor exacto de alguno de los dos números.
print("Hola usuario, ingresa dos números enteros para determinar si la diferencia entre los dos es un número divisor exacto de alguno de los dos.")

Numero1=int(input("Ingrese el primer número por favor: "))
Numero2=int(input("Ingrese el segundo número por favor: "))
resultado=Numero1-Numero2
if Numero1%resultado==0:
    print("La diferencia de los números ingresados es divisor entero del primer número")
if Numero2%resultado==0:
    print("La diferencia de los números es divisor entero del segundo número.")
if Numero1%resultado!=0:
    print("La diferencia de los números ingresados no es divisor entero del primer número")
if Numero2%resultado!=0:
    print("La diferencia de los números no es divisor entero del segundo número.")