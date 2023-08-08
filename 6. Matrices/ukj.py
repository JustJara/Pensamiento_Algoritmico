
def suma_matrices(A,B):
    cantidad_filasA=0
    for i in range(0,len(A),1):
        cantidad_columnasA=0
        for j in range(0,len(A[i]),1):
            cantidad_columnasA+=1
        cantidad_filasA+=1
    cantidad_filasB=0

    for i in range(0,len(B),1):
        cantidad_columnasB=0
        for j in range(0,len(B[i]),1):
            cantidad_columnasB+=1
        cantidad_filasB+=1

    if cantidad_columnasA!=cantidad_columnasB and cantidad_filasA!=cantidad_columnasB:
        print("ValueError(No es posible realizar la suma de matrices ya que la matriz A tiene",cantidad_filasA," filas y",cantidad_columnasA," columnas, mientras que la matriz B tiene",cantidad_filasB,"  filas y ",cantidad_columnasB," columnas")
    else:

    

        matriz_suma = []

        for i in range(len(A)):
            fila = []

            for j in range(len(A[i])):

                suma = A[i][j] + B[i][j]
                fila.append(suma)

            matriz_suma.append(fila)

        return matriz_suma
A = [[1,1],
    [2,1],
    [0,1]]

B = [[1,2],
    [2,0],
    [0,-1]]
    
print(suma_matrices(A,B))