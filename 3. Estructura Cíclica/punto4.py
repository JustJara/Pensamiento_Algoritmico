#Leer dos números enteros y determinar si la diferencia entre los dos es un número primo.
print("Hola usuario, te pediré dos números enteros para determinar si la diferencia entre ellos es un número primo")
num1 = int(input("Ingresa el primer número"))
num2 = int(input("Ingresa el segundo número"))
contadordivisores= 0
if num1>num2:
    dif= num1-num2
elif num2>num1:
    dif= num2-num1
print("La diferencia entre los números ingresados es: ",dif)

for i in range(1,dif+1,1):
    if dif%i==0:
        contadordivisores = contadordivisores+1
if contadordivisores <=2:
    print(dif," Es un número primo")
elif contadordivisores >=3:
    print(dif," No es un número primo")

