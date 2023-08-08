def ventas_mensuales_fabrica(matriz):
    ventas_mensuales_fabricat=[]
    for i in range(0,12,1):
        sumatoriaMes=0
        for j in range(0,5,1):
            sumatoriaMes+= matriz[j][i]
        ventas_mensuales_fabricat.append(sumatoriaMes)
    return ventas_mensuales_fabricat