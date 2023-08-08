def Mayor_venta_x_dep(matriz,departamento):
    mayor=0
    departamento-=1
    for i in range(0,len(matriz[departamento]),1):
        if matriz[departamento][i]>mayor:
            mayor=matriz[departamento][i]
            posicionmayor=i+1
    return posicionmayor
