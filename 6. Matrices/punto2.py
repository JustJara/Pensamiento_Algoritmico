m= int(input("Ingrese el número de índices que desea que tenga la matriz: "))
n= int(input("Ingrese el número de filas que desea que tenga la matriz: "))
x= int(input("Ingresa el rango máximo para que se genere un número aleatorio que estará en la matriz: "))
matriz=[]
import random
for i in range(0,n,1):
    fila=[]
    for j in range(0,m,1):
        fila.append(random.randint(0,x))
    matriz.append(fila)
print("Esta es la matriz resultante: ",matriz)