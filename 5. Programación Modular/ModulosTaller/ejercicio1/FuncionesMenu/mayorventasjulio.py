def mayor_ventas_julio(matriz):
    mayor=0
    for i in range(0,5,1):
        if matriz[i][6]>mayor:
            mayor=matriz[i][6]
            posicion_mayor=i+1
    return posicion_mayor
