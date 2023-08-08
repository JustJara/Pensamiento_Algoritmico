matriz_a = [[8,76,89,65],[34,65,87,23],[5,6,43,56],[1,4,6,23]]
matriz_b = [[91,84,75,26],[65,47,83,29],[10,43,23,76],[1,2,32,12]]
matriz_suma= []
for i in range(0,len(matriz_a),1):
    fila=[]
    for j in range(0,len(matriz_a[i]),1):
        fila.append(matriz_a[i][j]+matriz_b[i][j])
    matriz_suma.append(fila)
print("suma: ",matriz_suma)

matriz_resta=[]
for i in range(0,len(matriz_a),1):
    fila=[]
    for j in range(0,len(matriz_a[i]),1):
        fila.append(matriz_a[i][j]-matriz_b[i][j])
    matriz_resta.append(fila)
print("resta: ",matriz_resta)