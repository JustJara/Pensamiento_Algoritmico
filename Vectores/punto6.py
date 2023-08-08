lista=[56, 22, 12, 74, 23, 10, 68, 3, 44, 73, 79, 45, 7, 20, 89, 63, 20, 62, 25, 69, 63, 16, 20, 69, 1, 42, 18, 57, 47, 83, 93, 14, 36, 17, 84, 7, 3, 97, 80, 74, 11, 80, 49, 53, 89, 29, 9, 74, 48, 87]
contador_divisores=0
cantidad_numeros_primos=0
suma_primos=0
for i in range(0,len(lista),1):
    num = lista[i]
    for j in range(1,num,1):
        if num%j==0:
            contador_divisores+=1
    if contador_divisores<=2:
        suma_primos+= lista[i]
        print(lista[i])
        cantidad_numeros_primos+=1
    contador_divisores=0
promedio_primos=suma_primos/cantidad_numeros_primos
print("El promedio de los números primos que hay en la lista, es: ", promedio_primos)