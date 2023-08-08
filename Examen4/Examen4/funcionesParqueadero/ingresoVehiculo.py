def ingreso_vehiculo(parqueadero):
    print("Ingresa la posicion en la cual quieres que el vehiculo estacione")
    i=int(input("Ingrese el indice de la fila: "))
    j=int(input("Ingrese el indice de la columna: "))
    if parqueadero[i][j]==1:
        print("Ups, lo sentimos, este parqueadero en este momento está ocupado, intenta verificar cuál parqueadero esta libre con la opción 1")
    else:
        parqueadero[i][j]=1
        print("Tu vehiculo quedo parqueado en la posicion: ",i,j)
    
    return parqueadero