#Leer un número entero y si es múltiplo de 4 mostrar en pantalla su mitad, si es múltiplo de 5 mostrar en pantalla su cuadrado y si es múltiplo e 6 mostrar en pantalla su primer dígito. Asumir que el número no es mayor que 100.
print("Hola usuario, dame un número entero menor a 100 y si este es múltiplo de 4 entonces te diré cuál es la mitad; si es múltiplo de 5 te mostraré el cuadrado y si es múltiplo de 6 te mostraré cuál es el primer digito.")
Numero=int(input("Ingresa el número por favor: "))
if Numero>=100:
    print("El número no cumple con las condiciones especificadas")
else:
    if Numero%4==0:
        mitad=Numero/2
        print("Como ",Numero," es múltiplo de 4, entonces la mitad es: ",mitad)
    if Numero%5==0:
        cuadrado=Numero**2
        print("Como ",Numero," es múltiplo de 5, entonces el cuadrado de ",Numero," es ",cuadrado)
    if Numero%6==0:
        if Numero<10:
            primerDigito= Numero//10
            print("Como ",Numero, "es múltiplo de 6, entonces el primer digito es: ",primerDigito)

        
