"""Crea una matriz que contenga la tabla de multiplicar del 1 al 10 (11 filas y 11 
columnas). La primera fila y la primera columna debe contener estos números. Algo 
así:"""


matriz=[]
filas=11    
columnas=11
for i in range(0,columnas,1):
    fila=[]
    for j in range(0,1,1):
        fila.append(i)
    matriz.append(fila)

for k in range(0,10,1):
    for h in range(0,10,1):
        matriz[k][h]=k*h
print(matriz)
