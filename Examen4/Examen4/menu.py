estado_programa=True
parqueadero=[]
for i in range(0,3,1):
    fila=[]
    for j in range(0,4,1):
        fila.append(0)
    parqueadero.append(fila)

import funcionesParqueadero.espacioDisponibles as disponibles
import funcionesParqueadero.ingresoVehiculo as ingreso
import funcionesParqueadero.salidaVehiculo as salida
import funcionesParqueadero.estadoParqueadero as estado
while estado_programa:
    print("_________________________________________________")
    print("Juan Carlos, que desea saber acerca del parqueadero.")
    print("Segun lo que necesites, selecciona el numero que se te indique.")
    print("")
    print("Presiona 1, si deseas saber cuales espacios estan libres.")
    print("Presiona 2, para realizar el ingreso de un vehiculo al parqueadero")
    print("Presiona 3, para realizar la salida de un vehiculo del parqueadero")
    print("Presiona 4, para ver el estado del parqueadero actualmente.")
    print("Presiona 5, si deseas salir del programa.")

    opcion=int(input("Ingresa la opcion deseada: "))
    print("_________________________________________________")
    if opcion==1:
        disponibles.espacio_libre_parqueadero(parqueadero)
        print("_________________________________________________")
    if opcion==2:
        ingreso.ingreso_vehiculo(parqueadero)
        print("_________________________________________________")
    if opcion==3:
        salida.salida_vehiculo(parqueadero)
        print("_________________________________________________")
    if opcion==4:
        estado.estado_parqueadero(parqueadero)
        print("_________________________________________________")
    if opcion==5:
        print("Nos vemos en el proximo incio, feliz dia.")
        estado_programa=False
        print("_________________________________________________")