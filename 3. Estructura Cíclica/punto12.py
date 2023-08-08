# Leer un número y calcularle su factorial.}

num= int(input("Ingrese el número para calcular su factorial: "))
factorial=1
for i in range(num,0,-1):
     factorial = factorial*i
print(factorial)
    