"""""
Leer dos números enteros y si la diferencia entre los dos es menor o igual a 10 entonces 
mostrar en pantalla todos los enteros comprendidos entre el menor y el mayor de los 
números leídos.
"""

num1=int(input("Ingre el primer número entero"))
num2=int(input("Ingre el segundo número entero"))

if num1-num2<=10:
    if num1>num2:
        print("Los enteros entre los números ingresados son:")
        for i in range(num2+1,num1):
            print(i)
    elif num2>num1:
        print("Los enteros entre los números ingresados son:")
        for j in range(num1+1,num2):
            print(j)
else:
    print("La diferencia entre los dos números no es menor o igual a 10.")