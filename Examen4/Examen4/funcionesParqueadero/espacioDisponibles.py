def espacio_libre_parqueadero(parqueadero):
    sumatoria=0
    for i in range(0,3,1):
        for j in range(0,4,1):
            sumatoria+=parqueadero[i][j]
            if parqueadero[i][j]==0:
                print("La posicion",i,j," esta disponible")
            elif sumatoria==12:
                print("En este momento no existen espacios libres para dejar un vehiculo.")
    return espacio_libre_parqueadero