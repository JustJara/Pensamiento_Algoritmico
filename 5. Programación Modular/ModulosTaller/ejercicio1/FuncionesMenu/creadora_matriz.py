def matriz():
    import random
    matriz=[]
    for departamentos in range(0,5,1):
        fila=[]
        for meses in range(0,12,1):
            fila.append(random.randint(10000,1000000))
        matriz.append(fila)
    return matriz