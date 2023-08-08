"""
Se define la serie de Fibonacci como la serie que comienza con los dígitos 1 y 0 y va 
sumando progresivamente los dos últimos elementos de la serie, así: 0 1 1 2 3 5 8 13 21 
34.......  Utilizando  el  concepto  de  ciclo  generar  la  serie  de  Fibonacci  hasta  llegar  o 
sobrepasas el número 10000. 
"""
semilla1 = 1
semilla2 = 1
print(semilla1)
for i in range(1,10000,1):
    print(semilla2)
    aux= semilla1+semilla2
    semilla1=semilla2
    semilla2=aux
