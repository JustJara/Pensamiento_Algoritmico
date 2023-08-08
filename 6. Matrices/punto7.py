matriz=[]
N = int(input("Ingrese el tamaño de la matriz"))
for i in range(0,N,1):
    fila=[]
    for j in range(0,N,1):
        if i%2==0 and j%2==0:
            fila.append(1)
        elif i%2!=0 and j%2!=0:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
print(matriz)