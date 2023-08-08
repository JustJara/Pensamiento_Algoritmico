nfilas=int(input("Ingrese el número de filas que desea que haya en la matriz: "))
matriz=[]
import random
for i in range(0,nfilas,1):
    fila=[]
    for j in range(0,2,1):
        fila.append(random.randint(0,500))
        if j==1:
            fila.append(fila[0]+fila[1])
    matriz.append(fila)
print(matriz)