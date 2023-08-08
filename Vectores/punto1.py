lista =[56, 22, 12, 74, 23, 10, 68, 3, 44, 73, 79, 45, 7, 20, 89, 63, 20, 62, 25, 69, 63, 16, 20, 69, 1, 42, 18, 57, 47, 83, 93, 14, 36, 17, 84, 7, 3, 97, 80, 74, 11, 80, 49, 53, 89, 29, 9, 74, 48, 87]

import Operaciones.metodoOrdenamientoSeleccion as seleccion

ListaOrdenada = seleccion.ordenar_por_seleccion(lista)

NumeroMayor= len(lista)-1
NumeroMenor= lista[0]
CantidadRepetidoNMayor=0
CantidadRepetidoNMenor=0

for i in range (0,len(lista),1):
    if lista[i]==NumeroMenor:
        CantidadRepetidoNMenor+=1
    if lista[i]==NumeroMayor:
        CantidadRepetidoNMayor+=1

print("El número mayor que se encuentra en la lista es= ",NumeroMayor,"Y el menor es= ",NumeroMenor)
print("La cantidad de veces que se repite el número mayor en la lista es: ",CantidadRepetidoNMayor, "Y la cantidad de veces que se repite el número menor es: ",CantidadRepetidoNMenor)

