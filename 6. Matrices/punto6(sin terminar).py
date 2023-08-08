matriz=[]
print("Hola usuario ingresa de que tamaño deseas que se cree la matriz")
N = int(input(()))
for i in range(0,N,1):
    fila=[]
    for j in range(0,N,1):
        if i==j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
print(matriz)