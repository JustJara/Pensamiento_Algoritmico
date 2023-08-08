
n = int(input("Ingrese n"))
matriz = []
semilla = 1
for i in range(0,n,1):
    fila = []
    fila.append(semilla)
    for j in range(0,n-1,1):
        semilla +=1
        if semilla == n+1:
            semilla = 1
        fila.append(semilla)
    matriz.append(fila)
print(matriz)