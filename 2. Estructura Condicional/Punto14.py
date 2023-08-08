#14. Leer tres números enteros y mostrarlos ascendentemente.
print("Hola usuario dame 3 número enteros y te los orgnizaré de menor a mayor.")
Numero1=int(input("Ingresa el primer número: "))
Numero2=int(input("Ingresa el segundo número: "))
Numero3=int(input("Ingresa el tercer número: "))
if Numero1>Numero2 and Numero2>Numero3:
    print(Numero3, "-",Numero2,"-",Numero1)
if Numero1>Numero3 and Numero3>Numero2:
    print(Numero2,"-",Numero3,"-",Numero1)
if Numero2>Numero3 and Numero3>Numero1:
    print(Numero1,"-",Numero3,"-",Numero2)
if Numero2>Numero1 and Numero1>Numero3:
    print(Numero3,"-",Numero1,"-",Numero2)
if Numero3>Numero2 and Numero2>Numero1:
    print(Numero1,"-",Numero2,"-",Numero3)
if Numero3>Numero1 and Numero1>Numero2:
    print(Numero2,"-",Numero1,"-",Numero3)