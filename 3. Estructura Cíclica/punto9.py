"""
Si 32768 es el tope superior para los números entero cortos, determinar cuál es el número 
primo más cercano por debajo de él
"""
print("Determinaré cuál es el número primo más cercano de 32768")

for i in range(32768,0,-1):
    contadordivisores=0
    for j in range(1,32768,1):
        if i%j==0:
            contadordivisores= contadordivisores+1
    if contadordivisores == 2:
        print(i)
        break