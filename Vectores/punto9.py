lista=[56, 22, 12, 74, 23, 10, 68, 3, 44, 73, 79, 45, 7, 20, 89, 63, 20, 62, 25, 69, 63, 16, 20, 69, 1, 42, 18, 57, 47, 83, 93, 14, 36, 17, 84, 7, 3, 97, 80, 74, 11, 80, 49, 53, 89, 29, 9, 74, 48, 87]
suma_numeros=0
for i in range(0,len(lista),1):
    suma_numeros+= lista[i]
print("El promedio de los números de la lista es: ",suma_numeros/len(lista))
