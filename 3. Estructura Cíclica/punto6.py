"""
Leer dos números y mostrar todos los números terminados en 4 comprendidos entre 
ellos.
"""
print("Dame dos número y te mostraré todos los números terminados en 4 comprendidos entre ellos")

num1=int(input("Ingrese el primer número por favor: "))
num2=int(input("Ingrese el segundo número por favor: "))

if num1>num2:
    ultimodigito=0
    print("Los números entre ellos cuyo digitos terminan en 4 son:")
    for i in range(num2,num1,1):
        if i%10==4:
            print(i)
if num2>num1:
    ultimodigito=0
    print("Los números entre ellos cuyo digitos terminan en 4 son:")
    for j in range(num1,num2,1):
        if j%10==4:
            print(j)