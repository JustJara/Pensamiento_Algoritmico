lista=[56, 22, 12, 74, 23, 10, 68, 3, 44, 73, 79, 45, 7, 20, 89, 63, 20, 62, 25, 69, 63, 16, 20, 69, 1, 42, 18, 57, 47, 83, 93, 14, 36, 17, 84, 7, 3, 97, 80, 74, 11, 80, 49, 53, 89, 29, 9, 74, 48, 87]
cantidad_numeros_pares=0
suma_numeros_pares=0
for i in range(0,len(lista),1):
    if lista[i]%2==0:
        print(lista[i])
        suma_numeros_pares+=lista[i]
        cantidad_numeros_pares+=1
print("El promedio de los numeros pares de la lista es: ", suma_numeros_pares/cantidad_numeros_pares)