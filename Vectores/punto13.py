#Escriba un algoritmo que cuente y muestre cuántas veces aparece cada elemento de la lista y la posición en el que está ese elemento
lista=[56, 22, 12, 74, 23, 10, 68, 3, 44, 73, 79, 45, 7, 20, 89, 63, 20, 62, 25, 69, 63, 16, 20, 69, 1, 42, 18, 57, 47, 83, 93, 14, 36, 17, 84, 7, 3, 97, 80, 74, 11, 80, 49, 53, 89, 29, 9, 74, 48, 87]
repetido=1
posicion_repetidos=""
for i in range(0,len(lista),1):
    for j in range(1,len(lista),1):
        if lista[i]==lista[j]:
            repetido+=1
    print("El número en la posición ",i,"se repite ",repetido,"veces.")
    repetido=0
