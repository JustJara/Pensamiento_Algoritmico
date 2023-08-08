def salida_vehiculo(parqueadero):
    print("En que posicion se encuentra el vechiulo que va a salir.")
    i=int(input("Ingrese el indice de la fila: "))
    j=int(input("Ingrese el indice de la columna: "))
    if parqueadero[i][j]==1:
        parqueadero[i][j]=0
        print("El vehiculo ha dejado libre la posicion",i,j)
    else:
        print("Dentro de la posicion ingresada no se encuentra ningun vehiculo parqueado")
    return parqueadero