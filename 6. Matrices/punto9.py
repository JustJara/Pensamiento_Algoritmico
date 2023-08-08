import random
M = int(input("Ingrese la cantidad de filas que tendrá la matriz: "))
N = int(input("Ingrese la cantidad de columnas que tendrá la matriz: "))
print("---------------------------------------------------------------")
matriz=[]

for i in range(0,M,1):
    fila=[]
    for j in range(0,N,1):
        fila.append(random.randint(0,10))
    matriz.append(fila)

print("Esta es la matriz: ",matriz)
print("---------------------------------------------------------------")


mayor = 0
menor = 999
suma_filas=[]
sumatotal=0
cantidad_datos=0

for k in range(0,len(matriz),1):
    suma_fila=0
    for l in range(0,len(matriz[k]),1):
        sumatotal+= matriz[k][l]
        cantidad_datos+=1
        suma_fila  += matriz[k][l]

        if matriz[k][l] > mayor:
            mayor = matriz[k][l]
            posicionmayorColumna= k 
            posicionmayorfila= l

        if matriz[k][l] < menor:
            menor = matriz[k][l]
            posicionMenorColumna= k
            posicionMenorFila= l

    suma_filas.append(suma_fila)
promedio=sumatotal/cantidad_datos

suma_columna=[]
for n in range(0,N,1):
    suma_columnas=0
    for m in range(0,M,1):
        suma_columnas+= matriz[m][n]
    suma_columna.append(suma_columnas)



print("Esta es la información que extraje de la matriz: ")
print("La posición donde está el mayor número de la matriz es: ",posicionmayorfila,posicionmayorColumna)
print("La posición donde está el menor número de la matriz es: ",posicionMenorFila,posicionMenorColumna)
print("El promedio de todos los número que están en la matriz es: ",promedio)
print("El mayor número que está en la matriz es: ",mayor)
print("El menor número que está en la matriz es: ",menor)
print("La suma total de los elemenots de cada fila (cada fila es una posicion en la nueva matriz): ",suma_filas)
print("La suma total de los elemenots de cada columna (cada columna es una posicion en la nueva matriz): ",suma_columna)

