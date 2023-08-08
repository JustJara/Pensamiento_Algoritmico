#34. Leer un número entero de 2 dígitos y si terminar en 1 mostrar en pantalla su primer dígito,si termina en 2 mostrar en pantalla la suma de sus dígitos y si termina en 3 mostrar en pantalla el producto de sus dos dígitos.
print("Hola usuario ingrese un número entero de 2 digitos y si este termina en 1, en pantalla te mostraré el primer digito, si este termina en 2 entonces en pantalla te mostraré la suma de los digitos y si termina en 3 mostraré en pantalla el producto de sus digitos.")
Numero=int(input("Ingrese el número por favor: "))
if Numero<=9 or Numero>=100:
    print("El número ingresado no cumple con las condiciones especificadas.")
else:
    primerDigito=Numero//10
    segundoDigito=Numero%10

    if segundoDigito==1:
        print("Como el número termina en 1, entonces el primer digito es: ",primerDigito)
    if segundoDigito==2:
        sumatoria=primerDigito+segundoDigito
        print("Como el número termina en 2, entonces el resultado de la suma de los digitos es: ",sumatoria)
    if segundoDigito==3:
        producto=primerDigito*segundoDigito
        print("Como el número termina en 3, entonces el producto de los digitos es: ",producto)
