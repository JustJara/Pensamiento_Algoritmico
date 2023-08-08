def estado_parqueadero(parqueadero):
    sumatoria=0
    for i in range(0,3,1):
        for j in range(0,4,1):
            sumatoria+=parqueadero[i][j]
            if parqueadero[i][j]==0:
                print("La posicion",i,j," esta disponible")
            else:
                print("La posicion",i,j," esta ocupada")
    return estado_parqueadero