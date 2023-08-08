"""
Leer un número entero y mostrar todos sus componentes numéricos o sea aquellos para 
quienes él sea un múltiplo.
"""

print("Hola usuario, dame un número entero y determinaré todos sus componentes numéricos")
num=int(input("Ingrese el número por favor: "))
print("Estos son los múltiplos del número que ingresaste:")
for i in range(1,num+1,1):
    if num%i==0:
        print(i)